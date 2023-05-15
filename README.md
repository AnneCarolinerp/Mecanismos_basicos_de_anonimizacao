Atividade prática

Objetivo: Anonimizar o dataset sobre crédito (credit_v1.csv) usando
operações básicas de anonimização.

1. Carregue o dado
2. Remova todos os atributos não utilizados nas questões abaixo
3. Embaralhe a coluna Month
4. Use uma máscara no SSN para transformar 821-00-0265 em 821-**-****
5. Generalize o atributo Ocuppation. {Scientist, Teacher, Engineer,
Developer}-&gt;Academic, {Lawyer, Doctor}-&gt;Service,
{Media_manager, Journalist}-&gt;Media
a. Qual é o Iloss do valor Academic?
6. Generalize o atributo idade para os intervalos [20-29], [30-39]...
a. Qual o Iloss do valor [20-29]?
7. Adicionar um ruído independente entre -1000 e 1000 no atributo
Annual_Income em cada registro
8. Reporte a diferença entre a média de Annual_Income
anonimizado para original
