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

// para solucionar o problema uma implementação do algoritmo de Gale Shapley
// foi elaborada com as devidas variações para comportar a dinamica das notas

// para solucionar o problema uma implementação do algoritmo de Gale Shapley
// foi elaborada com as devidas variações para comportar a dinamica das notas

// Uma struct é definida para representar cada aluno, com atributos para
// o nome, a nota desse aluno e os projetos nos quais ele deseja participar 

struct Aluno {

    int idx_projetos = 0;
    int nota;
    vector<string> projetos_desejados;
    string nome;

    // descrição de alguns operadores para esse struct
    // tornando possível realizar um sort em vetores com esse
    // tipo de elementos
    
    // Implementando comparadores entre alunos
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
// Outra struct é definida para representar cada projeto, com atributos representando o nome do projeto,
// a nota mínima necessária para participar do projeto e a quantidade de vagas no projeto
struct Projeto {

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pares;
    int nota_required;
    int can_add;
    string nome;
};


vector<Aluno> alunos;
map<string, Projeto> projetos;

void take_aluno(string s){

    // todas as linhas de entrada dos alunos seguem o seguinte padrão pré determinado:
    // (id do aluno):(projetos que está interessado) (nota do aluno)
    // com isso, para obter um melhor tratamento para essa entrada a dupla optou por implementar uma função
    // que irá realizar a separação adequada para a criação correta do objeto Aluno

    stringstream taking(s);

    Aluno aluno_act;

    string mid;

    // abaixo a informação entre os primeiros parenteses é retirada
    // essa informação é o id do aluno

    getline(taking, mid, '(');
    getline(taking, mid, ')');

    aluno_act.nome = mid;

    getline(taking, mid, ':');
    getline(taking, mid, '(');

    getline(taking, mid, ')');

    // a informação dos projetos é retirada e colocada em uma nova stream de bits
    // para realizar a retirada dos projetos em ordem de preferencia

    string aux = mid;

    stringstream taking1(aux);
    string mid1;

    getline(taking, mid, ' ');
    getline(taking, mid, '(');
    getline(taking, mid, ')');

    // como a nota pode apresentar apenas 3 valores que podem ser representados
    // por apenas um digito é valido realizar essa conversão diretamente sem
    // auxilio do conversor

    aluno_act.nota = mid[0] - '0';
    int notas_menores = 0;
    while(getline(taking1, mid1, ' ')) {

        // pega as strings entre os espaços

        string projeto = "";
        for(int i = 0; i < mid1.size(); i++){

            if(mid1[i] == ',') continue; // ignora-se a virgula possivelmente presente no residuo sem espaço

            projeto.push_back(mid1[i]);
        }

        aluno_act.projetos_desejados.push_back(projeto);
        if(projetos[projeto].nota_required <= aluno_act.nota){
            notas_menores++;
            // marcamos para cada aluno se ele pode ter pelo menos um projeto para propor
        }
    }

    if(notas_menores) alunos.push_back(aluno_act); 
    // se ele não tiver nenhum projeto para propor nem consideramos ele na solução
    // para fins de otimização
}

int convert_int(string s){

    int aux = 0, pot_10 = 1;

    // converte um inteiro representado por uma string para um int

    for(int i = s.size()-1; i > -1; i--){

        aux += (s[i] - '0')*pot_10;
        pot_10 *= 10;
    }
    return aux;
}
void take_projeto(string s){

    // para receber os dados de um determinado projeto o grupo adotou a mesma estrategia para a
    // extração dos dados de um aluno, então o padrão especificado é:
    // (id do projeto, capacidade, nota)

    stringstream taking(s);

    string mid;

    getline(taking, mid, '(');
    getline(taking, mid, ')');

    // extraimos a informação que está entre os parenteses e colocamos em uma nova stringstream
    // para extrair os valores adequados para o objeto Projeto

    stringstream taking1(mid);

    string mid1;

    Projeto projeto_act;

    int idx = 0;

    // optamos pelo auxilio de uma variavel idx para conseguirmos definir em qual parte
    // da sequencia especificada estamos

    while(getline(taking1, mid1, ' ')){

        string act = "";

        // extraindo as informações entre os espaços

        for(int i = 0; i < mid1.size(); i++){

            if(mid1[i] == ',') continue;

            // também ignorando os parenteses que possam estar presentes nessa parcela da string

            act.push_back(mid1[i]);
        }

        if(!idx){

            // caso idx seja zero no formato especificado temos o id do projeto

            projeto_act.nome = act;
            idx++;
            continue;
        } 

        if(idx == 1){

            // em idx igual a 1 pelo formato temos a capacidade desse projeto
            // para esse caso optamos por dar suporte para a inserção de uma capacidadae
            // com mais de 2 digitos, portanto usamos o conversor para gerar isso

            projeto_act.can_add = convert_int(act);
            idx++;
            continue;
        }

        // por fim, temos a nota que deve seguir o mesmo padrão dos alunos
        // e portanto é representado por apenas um digito

        idx++;
        projeto_act.nota_required = act[0] - '0';
    }

    projetos[projeto_act.nome] = projeto_act;
}

// Algoritmo de Gale Shapely, recebe como parâmetro uma fila representando os alunos e retorna
// o emparelhamento máximo estável de alunos e projetos
set<pair<string, string>> gale_shapley(queue<int>& q){

    set<pair<string, string>> ret;

    while(!q.empty()){

        int me = q.front(); q.pop();
        // Iremos olhar para o aluno atual e o primeiro projeto no qual ele ainda não tentou entrar
        Aluno &real_me = alunos[me];
        Projeto &project_now = projetos[real_me.projetos_desejados[real_me.idx_projetos]];

        // Caso a nota necessária para entrar no projeto seja maior do que a do aluno, vamos colocá-lo de volta 
        // na fila e olhar para o próximo projeto, caso ainda haja algum que ele deseja participar e não tenha tentado
        if(project_now.nota_required > real_me.nota) {
            real_me.idx_projetos++;
            if(real_me.idx_projetos < real_me.projetos_desejados.size()) q.push(me);
            else real_me.idx_projetos = 0;
            continue;
        }
        //Caso o projeto já esteja com as vagas cheias , vamos analisar se o aluno atual é melhor do que o pior aluno
        // do projeto , caso seja, vamos realizar essa troca de pares
        if(project_now.pares.size() == project_now.can_add) {

            auto bad_pairing = project_now.pares.top();
            if(bad_pairing.first < real_me.nota){

                ret.erase({project_now.nome, alunos[bad_pairing.second].nome});
                cout << "Retirando o par: Projeto " << project_now.nome << " Aluno " << alunos[bad_pairing.second].nome << '\n';
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
                cout << "Inserindo o par : Projeto " << project_now.nome << " " << " Aluno " << real_me.nome << '\n';
            } else {
                real_me.idx_projetos++;
                if(real_me.idx_projetos < real_me.projetos_desejados.size()){

                    q.push(me);
                } else{

                    real_me.idx_projetos = 0;
                }
            }
        } else {
            //Caso ainda haja vagas no projeto, vamos simplesmente realizar esse pareamento e 
            // colocar o aluno no projeto

            project_now.pares.push({real_me.nota, me});
            ret.insert({project_now.nome, real_me.nome});
            cout << "Inserindo o par : Projeto " << project_now.nome << " " << " Aluno " << real_me.nome << '\n';
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
    set<pair<string,string>> pares;
    // Realizam-se 10 permutações diferentes de alunos para rodar o algoritmo gale shapely e analisar
    // qual produz o melhor pareamento possível
    for(int i = 0; i < 10; i++){
        
        queue<int> q;
        cout << "Iteração " << i+1 << '\n';
        random_device rd;
        mt19937 g(rd());
        shuffle(perm.begin(), perm.end(), g);
        for(auto&[x, y] : projetos){

            while(!y.pares.empty()) y.pares.pop();
        }

        for(int i = 0; i < alunos.size(); i++) q.push(perm[i]);

        set<pair<string, string>> aux = gale_shapley(q);
        if(aux.size() > ans) {
            pares = aux;
            ans = aux.size();
        }
        cout << aux.size() << " pares: ";
        for(auto [proj, al] : aux) cout << proj << "-" << al << " ";
        cout << '\n';
    }

    cout << "MAIOR PAREAMENTO ENCONTRADO\n";
    cout << "Tamanho : " << ans << "\n";
    for(auto [proj, al] : pares) cout << proj << " " << al << '\n';
}