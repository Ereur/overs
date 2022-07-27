const begin_level = 3.31
const project_xp = 3360
const note = 125
const has_coa_bonus = false

var level_xp = [
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
];


function calculate_end_level(current_level, project_xp, note, has_coa_bonus) {
	// Get current_xp
	level_down = Math.floor(current_level);
	level_down_xp = level_xp[level_down].y;

	level_sup = Math.ceil(current_level);
	level_sup_xp = level_xp[level_sup].y;

	level_xp_total_current = level_sup_xp - level_down_xp;
	current_xp = level_down_xp + (level_xp_total_current * (current_level - Math.floor(current_level)));

	// Get project_xp_total
	project_xp = parseInt(project_xp);
	project_xp_total = project_xp * (parseInt(note) / 100);
	bonus_xp = 0;
	if (has_coa_bonus) {
		project_xp_total = project_xp_total + (project_xp_total * 0.042);
	}

	//Calculate Final Xp.
	final_xp = current_xp + project_xp_total;
	// Calculate Final level
	var i = 0;
	for (; i < level_xp.length; i++) {
		if (level_xp[i].y > final_xp) {
			break;
		}
	}
	min_xp = level_xp[i - 1].y;
	max_xp = level_xp[i].y;
	tmp_max_xp = max_xp - min_xp;
	tmp_final_xp = final_xp - min_xp;
	var final_level = parseInt(level_xp[i - 1].x) + (tmp_final_xp / tmp_max_xp);
	final_level = final_level.toFixed(2);

	var blackholesDays = 0;
	// Calculate Blackholes Days
	if (current_level < 8.41) {
		var xp_final_bh = 78909;
		if (final_xp > xp_final_bh) {
			final_xp = xp_final_bh;
		}
		blackholesDays = (Math.pow((final_xp / xp_final_bh), 0.45) - (Math.pow((current_xp / xp_final_bh), 0.45))) * 593;
	}

	return [final_level, blackholesDays]
}

var [final_level, blackholesDays] = calculate_end_level(begin_level, project_xp, note, has_coa_bonus);

console.log(final_level, blackholesDays)