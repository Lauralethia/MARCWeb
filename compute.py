def visualize_series(numExp,intervention,
    Q1a,Q1b,# Text titles
    Q2,
    Q3,Q4,Q5,Q6,Q7,# Q7 stakeholders
    Q3b,Q4b,Q5b,Q6b,
    Q3c,Q4c,Q5c,Q6c,
    Q8 # values from questions, 1 2 3 or 4
    ):
    # Code adapted from https://www.pythoncharts.com/matplotlib/radar-charts/
    import matplotlib.pyplot as plt
    import numpy as np

    labels = ['CLR', 'PNLRA', 'NRWRA']

    evalRes = ['Sample','Testing site','Task', 'Stimuli','Measures','Stakeholders']
    Qtot=[Q2,Q3,Q4,Q5,Q6,Q7]

    if numExp == 2:
      Qtot = Qtot[:-1] + [Q3b,Q4b,Q5b,Q6b,Q7]
      evalRes = evalRes[:-1] + ['2.TS','2.Task', '2.Stimuli','2.Measures','Stakeholders']

    if numExp == 3:
      Qtot = Qtot[:-1]+[Q3b,Q4b,Q5b,Q6b,Q3c,Q4c,Q5c,Q6c,Q7]
      evalRes = evalRes[:-1] + ['2.TS','2.Task', '2.Stimuli','2.Measures',
                '3.TS','3.Task', '3.Stimuli','3.Measures','Stakeholders']

    if intervention == 'Yes':
      Qtot = Qtot + [Q8]
      evalRes = evalRes + ['Intervention']

    # Q2,Sa: Sample; Q3,TS: Testing site; Q4,Ta: Task; Q5,St: Stimuli; Q6,M: Measures; Q7,Sk: Stakeholders; Q2.2,Sa: Sample; Q3.2,TS: Teesting site; 
    #                 Q4.2,Ta: Task; Q5.2,St: Stimuli; Q6.2,M: Measures; Q8.I: Intervention

    FA_val = [val for is_FA, val in zip([x == 1 for x in Qtot ], evalRes) if is_FA]
    FB_val = [val for is_FB, val in zip([x == 2 for x in Qtot ], evalRes) if is_FB]
    FC_val = [val for is_FC, val in zip([x == 3 for x in Qtot ], evalRes) if is_FC]

    def make_legend(FA_val,FB_val,FC_val):
        
        linea1 = r"$\bf{CLR:}$"+', '.join(FA_val)
        linea2 = r"$\bf{PNLRA:}$" +', '.join(FB_val) 
        linea3 = r"$\bf{NRWRA:}$" +', '.join(FC_val)
        
        if len(FA_val)>6:
            linea1 =  '\n'.join( (r"$\bf{CLR:}$" +','.join(FA_val[:6]),','.join(FA_val[6:])))
        if len(FB_val)>6:
            linea2 =  '\n'.join( (r"$\bf{PNLRA:}$" +','.join(FB_val[:6]),','.join(FB_val[6:])))
        if len(FC_val)>6:  
            linea3 =  '\n'.join( (r"$\bf{NRWRA:}$" +','.join(FC_val[:6]),','.join(FC_val[6:])))
        
        if len(FA_val)==0:
            linea1 =  ' '.join( (r"$\bf{CLR:}$" ,'none'))
        if len(FB_val)==0:
            linea2 =  ' '.join( (r"$\bf{PNLRA:}$" ,'none'))
        if len(FC_val)==0:  
            linea3 =  ' '.join( (r"$\bf{NRWRA:}$" ,'none'))

        legenda = '\n'.join((
        linea1,
        linea2,
        linea3))
        return(legenda)

    legenda = make_legend(FA_val,FB_val,FC_val)
    # Translate to factor values
    Tot =  Qtot.count(1) + Qtot.count(2) + Qtot.count(3)
    FA = Qtot.count(1)/Tot #1-A: Control factor
    FB = Qtot.count(2)/Tot #2-B: Subjective factor
    FC = Qtot.count(3)/Tot #3-C: Social factor
    values = [FA,FB,FC]

    # Calculate total score as result area / maximum area
    # Goes grom [0-1], 0 is for 'pure' factor, 1 to perfectly equilibrated experiment
    area = (FA*FB*np.sin(120))/2 + (FB*FC*np.sin(120))/2 +(FA*FC*np.sin(120))/2
    PerEquilArea = ((((Tot/3)/Tot)*((Tot/3)/Tot)*np.sin(120))/2)*3 # Maximun posible area (all load the same weight)

    TotScore = area/PerEquilArea

    textstr =     'CLR = ' + str(round(values[0]*100,1)) + \
              '% | PNLRA = ' + str(round(values[1]*100,1) )+ \
              '% | NRWRA = ' + str(round(values[2]*100,1)) + \
              '% | BS = ' + str(round(TotScore,2))


    #legenda = '\n'.join((
    #r'CLR = Controlled laboratory research | PNLRA = Partially naturalistic laboratory research approach',
    #r' NRWRA = Naturalistic real-world research approach | BS = Balance Score'))

    num_vars = len(labels)
    # Split the circle into even parts and save the angles
    # so we know where to put each axis.
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # The plot is a circle, so we need to "complete the loop"
    # and append the start value to the end.
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(polar=True))

    fig.suptitle('Behavior: ' + Q1a, fontsize=14, fontweight='bold', color='#4A4A4A')

    # Draw the outline of our data.
    ax.plot(angles, values, color='#fe630f', linewidth=1)
    # Fill it in.
    ax.fill(angles, values, color='#e08162', alpha=0.25)

    # Fix axis to go in the right order and start at 12 o'clock.
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Draw axis lines for each angle and label.
    ax.set_thetagrids(np.degrees(angles),  ['CLR', 'PNLRA', 'NRWRA','CLR'])

    # Go through labels and adjust alignment based on where
    # it is in the circle.
    for label, angle in zip(ax.get_xticklabels(), angles):
      if angle in (0, np.pi):
        label.set_horizontalalignment('center')
      elif 0 < angle < np.pi:
        label.set_horizontalalignment('left')
      else:
        label.set_horizontalalignment('right')
      
    # Set position of y-labels to be in the middle
    # of the first two axes.
    ax.set_rlabel_position(180 / num_vars)

    # Add some custom styling.
    # Change the color of the tick labels.
    ax.tick_params(colors='#222222')
    # Make the y-axis (0-100) labels smaller.
    ax.tick_params(axis='y', labelsize=8)
    # Change the color of the circular gridlines.
    ax.grid(color='#AAAAAA')
    # Change the color of the outermost gridline (the spine).
    ax.spines['polar'].set_color('#222222')
    # Change the background color inside the circle itself.
    ax.set_facecolor('#FAFAFA')

    # Add chart a title and summary.
    fig.subplots_adjust(top=0.85)
    def chunkstring(string, length):
      return (string[0+i:length+i] for i in range(0, len(string), length))
    Context_subtitle = list(chunkstring('Context: ' + Q1b, 45))
    Context_subtitle = '\n'.join(Context_subtitle)
    
    ax.set_title(Context_subtitle, y=1.08,color = '#6B6B6B')

    # place a text box in upper left in axes coords
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='#e08162', alpha=0.25)
    ax.text(0.5, -0.02, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='center')
    ax.text(0.5, -0.06, legenda,transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='center')
    #ax.set_aspect('equal')
    plt.tight_layout(pad=2.5)

    from io import BytesIO
    figfile = BytesIO()
    fig.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    import base64
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png.decode('utf8')

if __name__ == '__main__':
    visualize_series(numExp = 3,intervention = 'Yes',
      Q1a="Your study aim",Q1b="Context",# Text titles
      Q2=1, # Sample
      Q3=1, # Testing site
      Q4=1, # Task
      Q5=1, # Stimuli
      Q6=1, # Measures
      Q7=1, # Stakeholders

      Q3b=2,
      Q4b=2,
      Q5b=3,
      Q6b=2,
      Q3c=4,
      Q4c=3,
      Q5c=4,
      Q6c=4,
      # Interventon questions 
      Q8=1)
