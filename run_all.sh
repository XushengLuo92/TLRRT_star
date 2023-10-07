#!/bin/bash
#for n in 2000 # 600 800 1000
#do
#    for h in 0 1
#    do
#        echo "--# --------------------n = ${n}------------------------"
#        for ((m=1;m<=10;m++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/unbiased_TLRRT_star.py  ${n} ${h} ${m}
#        done
#    done
#done

#for n in 1000 #
#do
#    for h in 0 1
#    do
#        echo "--# --------------------n = ${n}------------------------"
#        for ((m=1;m<=10;m++))
#        do
#            /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/RRT*_LTL/OptPlan4MulR.py ${n} ${m} ${h}
#        done
#    done
#done



# case study 2
# --------RRT ----------

#for m in 5
#do
#    for r in 0.25 0.2 0.15 0.1
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/unbiased_TLRRT_star.py ${r} ${m}
##            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py ${r}
#        done
#    done
#done



#for m in 1
#do
#    for r in 0.25 0.2 0.15 0.1
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/unbiased_TLRRT_star.py ${r} ${m}
##            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py ${r}
#        done
#    done
#done



#
#for m in 500
#do
#    for r in  0.15 0.1
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=10;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/unbiased_TLRRT_star.py ${r} ${m}
#    #        /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py ${r}
#        done
#    done
#done
# ------ SMC ---------
#for h in 17
#do
#    echo "--# --------------------h = ${h}------------------------"
#    for r in  0.1
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/RRT*_LTL/SMT4MulR.py ${r} ${h}
#        done
#    done
#done

#
#for  r in 0.15
#do
#    echo "--# --------------------r = ${r}------------------------"
#    for ((n=1;n<=5;n++))
#    do
#        /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/RRGLTL/new_OptPlan4MulR.py  ${r}
#    done
#done
#
#for  r in 0.1
#do
#    echo "--# --------------------r = ${r}------------------------"
#    for ((n=1;n<=10;n++))
#    do
#        /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/RRGLTL/new_OptPlan4MulR.py  ${r}
#    done
#done


#for m in 5
#do
#    for r in 0.25 0.2
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py ${r} ${m}
#        done
#
#        echo "--# --------------------r = ${r}------------------------"
#
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/unbiased_TLRRT_star.py ${r} ${m}
#        done
#        echo "--# --------------------r = ${r}------------------------"
#
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/RRGLTL/new_OptPlan4MulR_with_mul_final.py ${r} ${m}
#        done
#
#    done
#done


#for m in 5
#do
#    for r in 0.15 0.1
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py ${r} ${m}
#        done
#    done
#done
#
#for m in 5
#do
#    for r in 0.15 0.1
#    do
#       echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/unbiased_TLRRT_star.py ${r} ${m}
#        done
#    done
#done


#for m in 5
#do
#    for r in 0.15
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/RRGLTL/new_OptPlan4MulR_with_mul_final.py ${r} ${m}
#        done
#    done
#done
#

#for m in 5 1
#do
#    for r in 0.25 0.2 0.1
#    do
#        echo "--# --------------------r = ${r}------------------------"
#        for ((n=1;n<=5;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/iterative_temporal_motion_planning.py ${r} ${m}
#        done
#    done
#done

## case 3
for m in 7
do
    echo "----------------------r = ${m}------------------------"
    for n1 in 1 2 3
    do
        for n2 in 1 2 3
        do
            for n3 in 1 2 3
            do
               /usr/local/opt/python@3.8/bin/python3 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py ${m} ${n1} ${n2}
            done
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/SMC.py  ${m} ${n1} ${n2}
        done
    done
done


#for r in 0.02
#    do
#        for ((n=1;n<=20;n++))
#        do
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py ${r}
#            /usr/local/Cellar/python/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chrislaw/Github/TLRRT_star/SMC.py ${r}
#
#        done
#    done

#for ((n=1;n<=20;n++))
#do
#    /usr/local/opt/python@3.8/bin/python3 /Users/chrislaw/Github/TLRRT_star/biased_TLRRT_star.py
#done
