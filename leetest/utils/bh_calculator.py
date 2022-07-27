import math

level_xp = [
	{'x':0, 'y':0},
	{'x':1, 'y':462},
	{'x':2, 'y':2688},
	{'x':3, 'y':5885},
	{'x':4, 'y':11777},
	{'x':5, 'y':29217},
	{'x':6, 'y':46255},
	{'x':7, 'y':63559},
	{'x':8, 'y':74340},
	{'x':9, 'y':85483},
	{'x':10, 'y':95000},
	{'x':11, 'y':105630},
	{'x':12, 'y':124446},
	{'x':13, 'y':145782},
	{'x':14, 'y':169932},
	{'x':15, 'y':197316},
	{'x':16, 'y':228354},
	{'x':17, 'y':263508},
	{'x':18, 'y':303366},
	{'x':19, 'y':348516},
	{'x':20, 'y':399672},
	{'x':21, 'y':457632},
	{'x':22, 'y':523320},
	{'x':23, 'y':597786},
	{'x':24, 'y':682164},
	{'x':25, 'y':777756},
	{'x':24, 'y':682164},
	{'x':25, 'y':777756},
	{'x':26, 'y':886074},
	{'x':27, 'y':1008798},
	{'x':28, 'y':1147902},
	{'x':29, 'y':1305486},
	{'x':30, 'y':1484070}
]

def bh_calculator(current_level, project_xp, note, has_coa_bonus):
	# Get current_xp
	level_down = math.floor(current_level)
	level_down_xp = level_xp[level_down].get('y')

	level_sup = math.ceil(current_level)
	level_sup_xp = level_xp[level_sup].get('y')

	level_xp_total_current = level_sup_xp - level_down_xp
	current_xp = level_down_xp + (level_xp_total_current * (current_level - math.floor(current_level)))

	# Get project_xp_total
	project_xp = int(project_xp)
	project_xp_total = project_xp * (int(note) / 100)
	if (has_coa_bonus):
		project_xp_total = project_xp_total + (project_xp_total * 0.042)

	# Calculate Final Xp.
	final_xp = current_xp + project_xp_total

	# Calculate Final level
	i = 0
	while i < len(level_xp):
		if (level_xp[i].get('y') > final_xp):
			break
		i += 1
	min_xp = level_xp[i - 1].get('y')
	max_xp = level_xp[i].get('y')
	tmp_max_xp = max_xp - min_xp
	tmp_final_xp = final_xp - min_xp
	final_level = int(level_xp[i - 1].get('x')) + (tmp_final_xp / tmp_max_xp)
	final_level = round(final_level, 2)

	# Calculate Blackholes Days
	if current_level < 8.41:
		xp_final_bh = 78909
		if (final_xp > xp_final_bh):
			final_xp = xp_final_bh
		blackholesDays = (math.pow((final_xp / xp_final_bh), 0.45) - (math.pow((current_xp / xp_final_bh), 0.45))) * 593

	return [final_level, blackholesDays]
