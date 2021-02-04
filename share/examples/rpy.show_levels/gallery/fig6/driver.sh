# Load cmoi base ssm domaine
rpy.show_levels -i \
   $CMCGRIDF/prog/reghyb/$(date +%Y%m%d00)_000\
   --vcode\
   --pbot_graph 70000\
   --ptop_graph 1000\
   --title ETIKET\
   --plot_width 10\
   --out fig6.png
