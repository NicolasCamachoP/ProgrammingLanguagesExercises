;1.	Cree las funciones en el archivo base que le permitirán probar sus funciones y le facilitarán algunas partes.
(define (id x) 
  x
)
(define (neg x) 
  (- x)
)
(define (cuadrado x) 
  (* x x)
)
(define (cubo x) 
  (* x x x)
)
(define (neg-cubo x) 
  (neg
    (* x x x)
  )
)
(define (seno x)
  (sin x)
)
(define (racional-simple x)
  (/ 1 x)
)
(define (racional x)
  (/ 
    1 
    (+ 
      (* x x)
      1
    )
  )
)
(define (uno-menos-neg x)
  (- 1 (neg x))
)
;2.	[10%] Cree una función llamada evaluar-puntos cuyos argumentos son una función y una lista y retorna una lista de listas en la cual cada elemento es una pareja (lista de 2 elementos) con el valor de x y de f(x).
(define evaluar-puntos (lambda (f lista)
    (if (null? lista)
      (list)
      (cons
        (list
          (car lista) 
          (f (car lista))
        ) 
        (evaluar-puntos 
          f (cdr lista)
        )
      )
    )
  )
)
;3.	[20%] Cree una función es-creciente-en-punto?, la cual recibe una función y un número x y retorna verdadero si la función es creciente en el punto x. Para esto compare los valores de f(x), f(x-1) y f(x+1). Si f(x-1)<=f(x)<=f(x+1), la función es creciente en el punto x.
(define es-creciente-en-punto? (lambda (f x)
    (if (and (<= (f (- x 1)) (f x)) (<= (f x) (f (+ x 1))))
      #t 
      #f
    )
  )
)
;4.	[20%] Cree una función es-decreciente-en-punto? Análoga a la anterior. Es decir verdadero si f(x-1)>=f(x)>=f(x+1).
(define es-decreciente-en-punto? (lambda (f x)
    (if (and (>= (f (- x 1)) (f x)) (>= (f x) (f (+ x 1))))
      #t 
      #f
    )
  )
)
;5.	[20%] Cree una función es-creciente-en-muestra?, la cual tiene como argumento una función f y una lista de valores, y retorna verdadero si f(x) es creciente en TODOS los valores de la lista.
(define es-creciente-en-muestra? (lambda (f lista)
    (if (null? lista)
      #t
      (and 
        (es-creciente-en-punto? f (car lista)) 
        (es-creciente-en-muestra? f (cdr lista))
      )
    )
  )
)
;6.	[20%] Cree una función es-decreciente-en-muestra?, la cual tiene como argumento una función f y una lista de valores, y retorna verdadero si f(x) es decreciente en TODOS los valores de la lista.
(define es-decreciente-en-muestra? (lambda (f lista)
    (if (null? lista)
      #t
      (and 
        (es-decreciente-en-punto? f (car lista)) 
        (es-decreciente-en-muestra? f (cdr lista))
      )
    )
  )
)
;7.	[10%] Cree una función es-monotona?, la cual tiene como argumento una función f y una lista de valores, y retorna verdadero si f(x) es creciente o decreciente en TODOS los valores de la lista.
(define es-monotona? (lambda (f lista)
    (if (es-creciente-en-muestra? f lista)
      #t
      (if (es-decreciente-en-muestra? f lista)
        #t
        #f
      )
    )
  )
)