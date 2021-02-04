#==============================================
# Load vgridutils to get program d.vgrid_sample
#----------------------------------------------

#====================
# Vcode 5005 and 5100
#--------------------

cd ${TMPDIR}

cat > vgrid_sample.nml <<EOF
&cfg

  vc_5005%rcoef1=1
  vc_5005%rcoef2=2
  vc_5005%hyb_flat=-1.

  vc_5100%rcoef1=1
  vc_5100%rcoef2=2
  vc_5100%rcoef3=0
  vc_5100%rcoef4=100
  vc_5100%hyb_flat=-1.

/
EOF

OUT=out_5005_5100
rm -rf ${OUT}; d.vgrid_sample -out_dir ${OUT}

# The goal is to make the top 3 level flat. To know which hyb value
# is at level 3 type
# d.print_toctoc -fst out_5005_5100/5005 -convip
# d.print_toctoc -fst out_5005_5100/5100 -convip
# Here I found 0.0500000007450581 for both 5005 and 5100
# 0.05 will do
hyb_flat=0.05
cat > vgrid_sample.nml <<EOF
&cfg

  vc_5005%rcoef1=1
  vc_5005%rcoef2=2
  vc_5005%hyb_flat=${hyb_flat}

  vc_5100%rcoef1=1
  vc_5100%rcoef2=2
  vc_5100%rcoef3=0
  vc_5100%rcoef4=100
  vc_5100%hyb_flat=${hyb_flat}

/
EOF

OUT=out_5005_5100_flat
rm -rf ${OUT}; d.vgrid_sample -out_dir ${OUT}

rpy.show_levels --vcode -i\
		   out_5005_5100/5005\
		   out_5005_5100_flat/5005\
		   out_5005_5100/5100\
		   out_5005_5100_flat/5100\
		   --legend_text_spacing .1\
		   --ptop_graph 1000\
		   --plot_thermo\
		   -o hyb_pres_CP\
		   --title Hyb_pressure_C.P. Hyb_pressure_C.P._hyb_flat_${hyb_flat} Hyb_pressure_C.P._SLEVE Hyb_pressure_C.P._SLEVE_hyb_flat_${hyb_flat}

#============
# Vcode 21001
#------------
hyb_flat=20493.2
cat > vgrid_sample.nml <<EOF
&cfg

  vc_21001_NON_SLEVE%rcoef1=1
  vc_21001_NON_SLEVE%rcoef2=2
  vc_21001_NON_SLEVE%hyb_flat=-1.

  vc_21001_SLEVE%rcoef1=1
  vc_21001_SLEVE%rcoef2=2
  vc_21001_SLEVE%rcoef3=0
  vc_21001_SLEVE%rcoef4=100
  vc_21001_SLEVE%hyb_flat=-1.

/
EOF

OUT=out_21001
rm -rf ${OUT}; d.vgrid_sample -out_dir ${OUT}

# The goal is to make the top 3 level flat. To know which hyb value
# is at level 3 type:
# d.print_toctoc -fst out_21001/21001_NON_SLEVE -convip
# Here I found 20493.1992187500
# 20493.2 will do
hyb_flat=20493.2

cat > vgrid_sample.nml <<EOF
&cfg

  vc_21001_NON_SLEVE%rcoef1=1
  vc_21001_NON_SLEVE%rcoef2=2
  vc_21001_NON_SLEVE%hyb_flat=${hyb_flat}

  vc_21001_SLEVE%rcoef1=1
  vc_21001_SLEVE%rcoef2=2
  vc_21001_SLEVE%rcoef3=0
  vc_21001_SLEVE%rcoef4=100
  vc_21001_SLEVE%hyb_flat=${hyb_flat}

/
EOF
OUT=out_21001_flat
rm -rf ${OUT}; d.vgrid_sample -out_dir ${OUT}

rpy.show_levels --vcode -i\
		   out_21001/21001_NON_SLEVE\
		   out_21001_flat/21001_NON_SLEVE\
		   out_21001/21001_SLEVE\
		   out_21001_flat/21001_SLEVE\
		   --legend_text_spacing .1\
		   --ptop_graph 1000\
		   --plot_thermo\
		   -o hyb_Height_GC\
		   --title Hyb_Height_Gal_Chen Hyb_Height_Gal_Chen_hyb_flat_${hyb_flat} Hyb_Height_Gal_Chen_SLEVE Hyb_Height_Gal_Chen_SLEVE_hyb_flat_${hyb_flat}

#============
# Vcode 21002
#------------
cat > vgrid_sample.nml <<EOF
&cfg

  vc_21002_NON_SLEVE%rcoef1=1
  vc_21002_NON_SLEVE%rcoef2=2
  vc_21002_NON_SLEVE%hyb_flat=-1.

  vc_21002_SLEVE%rcoef1=1
  vc_21002_SLEVE%rcoef2=2
  vc_21002_SLEVE%rcoef3=0
  vc_21002_SLEVE%rcoef4=100
  vc_21002_SLEVE%hyb_flat=-1.

/
EOF

OUT=out_21002
rm -rf ${OUT}; d.vgrid_sample -out_dir ${OUT}

# The goal is to make the top 3 level flat. To know which hyb value
# is at level 3 type:
# d.print_toctoc -fst out_21002/21002_NON_SLEVE -convip
# Here I found again 20493.1992187500
# 20493.2 will do
hyb_flat=20493.2

cat > vgrid_sample.nml <<EOF
&cfg

  vc_21002_NON_SLEVE%rcoef1=1
  vc_21002_NON_SLEVE%rcoef2=2
  vc_21002_NON_SLEVE%hyb_flat=${hyb_flat}

  vc_21002_SLEVE%rcoef1=1
  vc_21002_SLEVE%rcoef2=2
  vc_21002_SLEVE%rcoef3=0
  vc_21002_SLEVE%rcoef4=100
  vc_21002_SLEVE%hyb_flat=${hyb_flat}

/
EOF
OUT=out_21002_flat
rm -rf ${OUT}; d.vgrid_sample -out_dir ${OUT}

rpy.show_levels --vcode -i\
		   out_21002/21002_NON_SLEVE\
		   out_21002_flat/21002_NON_SLEVE\
		   out_21002/21002_SLEVE\
		   out_21002_flat/21002_SLEVE\
		   --legend_text_spacing .1\
		   --ptop_graph 1000\
		   --plot_thermo\
		   --plot_vertical_velocity\
		   -o hyb_Height_Lorenz\
		   --title Hyb_Height_Lorenz Hyb_Height_Lorenz_flat_${hyb_flat} Hyb_Height_Lorenz_SLEVE Hyb_Height_Lorenz_SLEVE_hyb_flat_${hyb_flat}
