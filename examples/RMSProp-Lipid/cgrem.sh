cgrem_rmsprop --ref model_ref.p --model model.txt \
      --cgderiv-arg cgderiv.sh --md md.in \
      --restart restart --table ./ \
      --optimizer builtin,chi=8e-3,begknots=1,endknots=3,maxstepsize=100,t=303.0,lr_decay=0.999,decay='exp',correct=True \
      --maxiter 1 
