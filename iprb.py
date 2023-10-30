def probability():
	k, m, n = 23, 19, 21
	rab = k+m+n

	k_ratio = k/rab
	kk = k_ratio*(k-1)/(rab-1)*1       #k is DD, so *1 for all 3 possibilities (it MUST contain at least one dominant D, according to Mendel laws)
	km = k_ratio*m/(rab-1)*1
	kn = k_ratio*n/(rab-1)*1

	m_ratio = m/rab    #m is Dd, so mk MUST at least 1 D; mm is DdxDd, so 3/4 possibility of at least 1D; mn is Ddxdd, so 1:2 has 1D (no, not 1D like OneDirection)
	mk = m_ratio*k/(rab-1)*1
	mm = m_ratio*(m-1)/(rab-1)*0.75
	mn = m_ratio*n/(rab-1)*0.5

	n_ratio = n / rab #n is dd, so in short, nk is DDxdd (every individual is Dd), nm ddxDd, so 1:2; ddxdd NOBODY has at least 1 D
	nk = n_ratio*k/(rab-1)*1
	nm = n_ratio*m/(rab-1)*0.5
	nn = n_ratio* (n-1)/(rab-1)*0

	result = kk+nn+mm+mn+nm+mk+nk+kn+km

	return result

prob= probability()

print(prob)