#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<sstream>
#include<fstream>

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

    priority_queue<Aluno> pares;
    int nota_required;
    int can_add;
    string nome;
};


vector<vector<Aluno>> alunos(3);
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

    while(getline(taking1, mid1, ' ')) {

        string projeto = "";
        for(int i = 0; i < mid1.size(); i++){

            if(mid1[i] == ',') continue;

            projeto.push_back(mid1[i]);
        }

        if(projetos[projeto].nota_required <= aluno_act.nota){

            aluno_act.projetos_desejados.push_back(projeto);
        }
    }

    alunos[aluno_act.nota - 3].push_back(aluno_act);
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
    
    for(int i = 0; i < 3; i++){

        for(auto x : alunos[i]){

            cout << x.nome << " " << x.nota << '\n';
        }
    }

    for(auto[x, y] : projetos){

        cout << x << " " << y.nome << " " << y.can_add << " " << y.nota_required << '\n';
    } 
}