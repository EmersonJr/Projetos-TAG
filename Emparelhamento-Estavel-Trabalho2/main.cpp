#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<set>
#include<random>

using namespace std;

struct Aluno {

    int idx_projetos = 0;
    int nota;
    vector<string> projetos_desejados;
    string nome;

    bool operator<(const Aluno& a) const {
        int x = a.projetos_desejados.size();
        int y = a.nota;

        return(projetos_desejados.size() < x || nota < y);
    }

    bool operator>(const Aluno& a) const {
        int x = a.projetos_desejados.size();
        int y = a.nota;

        return(projetos_desejados.size() > x || nota > y);
    }

    bool operator==(const Aluno& a) const {
        int x = a.projetos_desejados.size();
        int y = a.nota;

        return(projetos_desejados.size() == x && nota == y);
    }
};

struct Projeto {

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pares;
    int nota_required;
    int can_add;
    string nome;
};


vector<Aluno> alunos;
map<string, Projeto> projetos;

void take_aluno(string s){

    stringstream taking(s);

    Aluno aluno_act;

    string mid;

    getline(taking, mid, '(');

    getline(taking, mid, ')');

    aluno_act.nome = mid;

    getline(taking, mid, ':');
    getline(taking, mid, '(');

    getline(taking, mid, ')');

    string aux = mid;

    stringstream taking1(aux);
    string mid1;

    getline(taking, mid, ' ');
    getline(taking, mid, '(');
    getline(taking, mid, ')');

    aluno_act.nota = mid[0] - '0';
    int notas_menores = 0;
    while(getline(taking1, mid1, ' ')) {

        string projeto = "";
        for(int i = 0; i < mid1.size(); i++){

            if(mid1[i] == ',') continue;

            projeto.push_back(mid1[i]);
        }

        aluno_act.projetos_desejados.push_back(projeto);
        if(projetos[projeto].nota_required <= aluno_act.nota){
            notas_menores++;
        }
    }

    if(notas_menores < aluno_act.projetos_desejados.size()) alunos.push_back(aluno_act);
}

int parse_int(string s){

    int aux = 0, pot_10 = 1;

    for(int i = s.size()-1; i > -1; i--){

        aux += (s[i] - '0')*pot_10;
        pot_10 *= 10;
    }
    return aux;
}
void take_projeto(string s){

    stringstream taking(s);

    string mid;

    getline(taking, mid, '(');
    getline(taking, mid, ')');

    stringstream taking1(mid);

    string mid1;

    Projeto projeto_act;

    int idx = 0;

    while(getline(taking1, mid1, ' ')){

        string act = "";

        for(int i = 0; i < mid1.size(); i++){

            if(mid1[i] == ',') continue;

            act.push_back(mid1[i]);
        }

        if(!idx){

            projeto_act.nome = act;
            idx++;
            continue;
        } 

        if(idx == 1){

            projeto_act.can_add = parse_int(act);
            idx++;
            continue;
        }

        idx++;
        projeto_act.nota_required = act[0] - '0';
    }

    projetos[projeto_act.nome] = projeto_act;
}

set<pair<string, string>> gale_shapley(queue<int>& q){

    set<pair<string, string>> ret;

    while(!q.empty()){

        int me = q.front(); q.pop();

        Aluno &real_me = alunos[me];
        Projeto &project_now = projetos[real_me.projetos_desejados[real_me.idx_projetos]];

        if(project_now.nota_required > real_me.nota) {
            real_me.idx_projetos++;
            if(real_me.idx_projetos < real_me.projetos_desejados.size()) q.push(me);
        }
        if(project_now.pares.size() == project_now.can_add) {

            auto bad_pairing = project_now.pares.top();
            if(bad_pairing.first < real_me.nota){

                ret.erase({project_now.nome, alunos[bad_pairing.second].nome});
                alunos[bad_pairing.second].idx_projetos++;
                if(alunos[bad_pairing.second].idx_projetos < alunos[bad_pairing.second].projetos_desejados.size()){

                    q.push(me);
                } else{

                    alunos[bad_pairing.second].idx_projetos = 0;
                }
                q.push(bad_pairing.second);
                project_now.pares.pop();
                project_now.pares.push({real_me.nota, me});
                ret.insert({project_now.nome, real_me.nome});
            } else {
                real_me.idx_projetos++;
                if(real_me.idx_projetos < real_me.projetos_desejados.size()){

                    q.push(me);
                } else{

                    real_me.idx_projetos = 0;
                }
            }
        } else {

            project_now.pares.push({real_me.nota, me});
            ret.insert({project_now.nome, real_me.nome});
        }
    } 

    return ret;
}

signed main() {

    string in, file_in = "in.txt";

    ifstream file(file_in);

    for(int i = 0; i < 55; i++){
        getline(file, in);
        take_projeto(in);
    }
    while(getline(file, in)){

        take_aluno(in);
    }

    sort(alunos.begin(), alunos.end());

    vector<int> perm(alunos.size());
    for(int i = 0; i < alunos.size(); i++) perm[i] = i;

    int ans = 0;

    for(int i = 0; i < 10; i++){
        
        queue<int> q;

        random_device rd;
        mt19937 g(rd());
        shuffle(perm.begin(), perm.end(), g);
        for(auto&[x, y] : projetos){

            while(!y.pares.empty()) y.pares.pop();
        }

        for(int i = 0; i < alunos.size(); i++) q.push(perm[i]);
        set<pair<string, string>> aux = gale_shapley(q);

        cout << aux.size() << " --- \n";
    }

}