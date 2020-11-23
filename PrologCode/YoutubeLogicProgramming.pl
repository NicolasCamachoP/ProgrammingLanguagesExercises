%Hechos
publica(shaun,[v1,v3]).
publica(doug,[v4]).
publica(jorge,[v2,v5,v6]).
publica(alvin,[v6,v7]).

like(juan, [v1, v2, v3]).
like(pedro, [v2, v4, v4]).
like(maria, [v3, v4, v1]).
like(ana, [v4, v5, v2]).
like(marta, [v3,v2]).
like(grumpy, []).

%Reglas
/* 1. (10%) Construya un predicado video(V) que indique si V es un video 
publicado por alguien. */
video(X) :- publica(_,Y) ,member(X, Y).
/* 2. (20%) Implemente el predicado jaccard, con tres parámetros, que 
indique si el tercer parámetro es el Indice de Jaccard  entre los 
2 primeros argumentos.  */
jaccard(S1, S2, X) :-
    sort(S1, L1),
    sort(S2,L2),
    intersection(L1,L2,I),
    union(L1,L2, U),
    length(I, SIZE1), 
    length(U, SIZE2),
    X is SIZE1/SIZE2.
/* 3. (15%) Implemente el predicado colabora(C1,C2), con dos parámetros, 
que sea verdadero los canales C1 y C2 tengan un video en común.  */
colabora(C1, C2) :-
    publica(C1, VIDEOS1),
    publica(C2, VIDEOS2),
    intersection(VIDEOS1, VIDEOS2, U),
    length(U, NVIDEOS),
    NVIDEOS>= 1,
    C1\==C2,!.
/* 4. (15%) Implemente el predicado afinidadLikes(U1,U2,A), con tres parámetros, 
que sea verdadero si el Índice de Jaccard entre los likes de U1 y de U2 es A.  */
afinidadLikes(U1, U2, A):-
    like(U1, L1),
    like(U2, L2),
    jaccard(L1, L2, X),
    A is X.
/* 5. (15%) Implemente el predicado canales(U1,C), con dos parámetros, 
que sea verdadero si en la lista C están ordenados y sin repetir (sort/2) 
los canales que publicaron los videos que le gustaron al usuario U1 .  */
/*findall(Canal,publica(Canal,_),Z).*/
videosde(V,C):- 
    publica(C,LV),
    intersection(LV, V, I),
    length(I, SI),
    SI>0.
canales(U1, C):-
    like(U1, LV),
    findall(X,videosde(LV, X),Z),
    sort(Z, Z1),
    C=Z1.
/* 6. (15%) Implemente el predicado afinidadCanales(U1,U2,A), con tres parámetros, 
que sea verdadero si el Índice de Jaccard entre los canales que le gustaron a U1 
y a U2 es A.  */
afinidadCanales(U1, U2, A):-
    canales(U1, C1),
    canales(U2, C2),
    jaccard(C1, C2, X),
    A is X.
/* 7. (10%) Implemente el predicado recomendarAmigo(U1,U2), con dos parámetros, 
que sea verdadero si la afinidad por canales o por likes entre U1 y U2 es mayor a 0.5.  */
recomendarAmigo(U1, U2):-
    afinidadCanales(U1, U2, X),
    afinidadLikes(U1, U2, Y),
    U1 \= U2,
    ( X > 0.5 ->  true; ( Y > 0.5 ->  true, false ) ), !.