# aws
always update to the latest parallel cluster

# after install
bashrc:
```
alias qstatf='squeue -o " %.18a,  %.18A, %.18B, %.18c, %.18C, %.18d, %.18D, %.18e, %.18E, %.18f, %.18F, %.18g, %.18G, %.18h, %.18H, %.18i, %.18I, %.30j, %.18J, %.18k, %.18K, %.18l, %.18L, %.18m, %.18M, %.18n, %.18N, %.80o, %.18O, %.18p, %.18P, %.18q, %.18Q, %.18r, %.18R, %.30S, %.18t, %.18T, %.18u, %.18U, %.18v, %.30V, %.18w, %.18W, %.18x, %.18X, %.18y, %.18Y, %.18z, %.90Z"'
alias qstats='echo ` squeue -o " %.5A, %.18B, %.4c, %.4C, %.4d, %.4D, %.18e, %.18E, %.18f, %.18F, %.5i,  %.20j, %.3J, %.18k, %.5K, %.18L, %.18m, %.18M, %.6n, %.6N,  %.3O, %.3p, %.5P, %.8q, %.18r, %.18R, %.30S,  %.18T, %.20V, %.80Z\n"` | tee qstat.tmp'
```