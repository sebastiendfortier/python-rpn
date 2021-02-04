VGRID_SAMPLE=${ATM_MODEL_DFILES}/bcmk_vgrid

rpy.show_levels -i \
   ${VGRID_SAMPLE}/5005\
   --vcode\
   --title ETIKET\
   --plot_delta\
   --ptop_graph 50000\
   --pbot_hill 101325\
   --ptop_hill 101325\
   --plot_thermo --plot_vertical_velocity\
   --legend_text_spacing .09\
   --legend_fraction .25\
   --plot_delta_sym\
   --out fig3.png
