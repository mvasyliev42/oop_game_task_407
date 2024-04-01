#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  Apr 01, 2024 09:35:20 AM CEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) white
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
set vTcl(project_theme) default



proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu $top.m53 -background #d9d9d9 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 600x521+433+131
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Toplevel 0"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    frame "$top.fra47" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 515 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 605 
    vTcl:DefineAlias "$top.fra47" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra47
    label "$site_3_0.lab49" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "Label" 
    vTcl:DefineAlias "$site_3_0.lab49" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button "$site_3_0.but48" \
        -activebackground #d9d9d9 -activeforeground black -background #d9d9d9 \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -text "Button" 
    vTcl:DefineAlias "$site_3_0.but48" "Button1" vTcl:WidgetProc "Toplevel1" 1
    entry "$site_3_0.ent51" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 224 
    vTcl:DefineAlias "$site_3_0.ent51" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label "$site_3_0.lab50" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "Label" 
    vTcl:DefineAlias "$site_3_0.lab50" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry "$site_3_0.ent52" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 224 
    vTcl:DefineAlias "$site_3_0.ent52" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.331 -y 0 -rely 0.315 -width 0 \
        -relwidth 0.238 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but48 \
        -in $site_3_0 -x 0 -relx 0.331 -y 0 -rely 0.697 -width 147 \
        -relwidth 0 -height 56 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent51 \
        -in $site_3_0 -x 0 -relx 0.281 -y 0 -rely 0.247 -width 224 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.331 -y 0 -rely 0.494 -width 0 \
        -relwidth 0.221 -height 0 -relheight 0.092 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent52 \
        -in $site_3_0 -x 0 -relx 0.281 -y 0 -rely 0.427 -width 224 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    frame "$top.fra55" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 515 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 595 
    vTcl:DefineAlias "$top.fra55" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra55
    label "$site_3_0.lab56" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "Label" 
    vTcl:DefineAlias "$site_3_0.lab56" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label "$site_3_0.lab57" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "Label" 
    vTcl:DefineAlias "$site_3_0.lab57" "Label4" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab56 \
        -in $site_3_0 -x 0 -relx 0.235 -y 0 -rely 0.272 -width 0 \
        -relwidth 0.292 -height 0 -relheight 0.08 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 0 -relx 0.235 -y 0 -rely 0.427 -width 0 \
        -relwidth 0.36 -height 0 -relheight 0.099 -anchor nw \
        -bordermode ignore 
    frame "$top.fra48" \
        -borderwidth 2 -relief groove -background #d9d9d9 -height 515 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 595 
    vTcl:DefineAlias "$top.fra48" "Frame3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra48
    label "$site_3_0.lab51" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "ID" 
    vTcl:DefineAlias "$site_3_0.lab51" "Label5" vTcl:WidgetProc "Toplevel1" 1
    button "$site_3_0.but54" \
        -activebackground #d9d9d9 -activeforeground black -background #d9d9d9 \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -text "Create game" 
    vTcl:DefineAlias "$site_3_0.but54" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button "$site_3_0.but55" \
        -activebackground #d9d9d9 -activeforeground black -background #d9d9d9 \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -text "Join game" 
    vTcl:DefineAlias "$site_3_0.but55" "Button3" vTcl:WidgetProc "Toplevel1" 1
    label "$site_3_0.lab52" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "Password" 
    vTcl:DefineAlias "$site_3_0.lab52" "Label6" vTcl:WidgetProc "Toplevel1" 1
    entry "$site_3_0.ent49" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 194 
    vTcl:DefineAlias "$site_3_0.ent49" "Entry3" vTcl:WidgetProc "Toplevel1" 1
    entry "$site_3_0.ent50" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 10" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -insertbackground #000000 -selectbackground #d9d9d9 \
        -selectforeground black -width 194 
    vTcl:DefineAlias "$site_3_0.ent50" "Entry4" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.336 -y 0 -rely 0.155 -width 0 \
        -relwidth 0.326 -height 0 -relheight 0.06 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but54 \
        -in $site_3_0 -x 0 -relx 0.336 -y 0 -rely 0.505 -width 87 -relwidth 0 \
        -height 36 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but55 \
        -in $site_3_0 -x 0 -relx 0.521 -y 0 -rely 0.505 -width 87 -relwidth 0 \
        -height 36 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.336 -y 0 -rely 0.33 -width 0 \
        -relwidth 0.108 -height 0 -relheight 0.041 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent49 \
        -in $site_3_0 -x 0 -relx 0.336 -y 0 -rely 0.233 -width 194 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent50 \
        -in $site_3_0 -x 0 -relx 0.336 -y 0 -rely 0.388 -width 194 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra47 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.008 -height 0 \
        -relheight 0.988 -anchor nw -bordermode ignore 
    place $top.fra55 \
        -in $top -x 0 -y 0 -width 0 -relwidth 0.992 -height 0 \
        -relheight 0.988 -anchor nw -bordermode ignore 
    place $top.fra48 \
        -in $top -x 0 -y 0 -rely 0.019 -width 0 -relwidth 0.992 -height 0 \
        -relheight 0.988 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

