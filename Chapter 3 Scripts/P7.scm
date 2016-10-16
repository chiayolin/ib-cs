; P7.scm
;
; Display the integer values 1–100 as given in question P6 using 
; Scheme (I run Scheme on Racket with SICP extension).
;
; date:    10/16/2016
; author:  Chiayo Lin
; license: GPL 3.0

#lang sicp

(define divisible? 
  (lambda (x y) 
    (= (remainder x y) 0)))

(define print-format
  (lambda (number right-algin)
    (if (= (string-length (number->string number)) right-algin)
      (display number)
      (begin
        (display " ")
        (print-format number (- right-algin 1))))))

(define print-row 
  (lambda (counter)    
    (print-format counter 4) 
    (if (divisible? counter 10) 
      (newline))
    (if (not (= counter 100)) 
      (print-row (+ counter 1)))))

(print-row 1)
