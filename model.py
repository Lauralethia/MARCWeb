from wtforms import Form, RadioField, validators,TextField, TextAreaField, SubmitField , IntegerField , BooleanField 


def indivQ(N):# Define the task related questions
        # TASK Q2
        TASK2 = TextField(label='Would you like to give your '+str(N)+' task a name?',default='No '+str(N)+' task')

        Q3b = RadioField(
            label='Task '+str(N)+'.3 If you have '+str(N)+' tasks, how its testing site reflects the context (R1a/b)?',
            coerce=int,
            choices=[(1,'CLR [Lab/ clinical testing room]'),
                    (2,'PNLRA [Lab set up to look like a classroom]'),
                    (3,'NRWRA [Classroom with little/no experimenter presence and interference into teaching activities]'),
                    (4,'No '+str(N)+' task')],
            default=4,
            validators=[validators.InputRequired()])   
        TQ3b = TextAreaField(label='Please justify your answer below.', default='No comment')

        Q4b = RadioField(
            label='Task '+str(N)+'.4. If you have '+str(N)+' task, how your task reflects that context?',
            coerce=int,
            choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                    (2,'PNLRA [Test of memory after viewing a movie]'),
                    (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]'),
                    (4,'No '+str(N)+'task')],

            default=4,
            validators=[validators.InputRequired()])
        TQ4b = TextAreaField(label='Please justify your answer below.', default='No comment')

        Q5b = RadioField(
            label='Task '+str(N)+'.5. If you have '+str(N)+' tasks, how your stimuli reflect that context?',
            coerce=int,
            choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                    (2,'PNLRA [Dynamic stimuli, like dynamic faces on video] '),
                    (3,'NRWRA [Fully naturalistically sampled stimuli: people during social interaction]'),
                    (4,'No '+str(N)+' stimuli')],
            default=4,
            validators=[validators.InputRequired()])
        TQ5b = TextAreaField(label='Please justify your answer below.',default='No comment')

        Q6b = RadioField(
            label='Task '+str(N)+'.6. If you have '+str(N)+' tasks, how your measures reflect that behavior?',
            coerce=int,
            choices=[(1,'CLR [Well-researched brain correlates of a specific cognitive process in typical conditions]'),
                    (2,'PNLRA [Canonical brain correlates in non-traditional laboratory settings and/or using more portable brain imaging tools]'),
                    (3,'NRWRA [Portable brain imaging tools in external environments to test for canonical brain correlates of cognitive processes]'),
                    (4,'No '+str(N)+' task')],
            default=4,
            validators=[validators.InputRequired()])
        TQ6b = TextAreaField(label='Please justify your answer below.', default='No comment')

        return (TASK2,Q3b,TQ3b,Q4b,TQ4b,Q5b,TQ5b,Q6b,TQ6b)

def interventionQ():# Define the intervention questions
    # INTERTITLE,Q8,TQ8,Q9,TQ9,Q10,TQ10,Q11,TQ11,Q12,TQ12 = interventionQ()
    INTERTITLE = TextField(label='Would you like to give your intervention a name?',default='No intervention title')   
    Q8 = RadioField(
        label='8. Related to intervention component, please indicate where your intervention fits in best.',
        coerce=int,
        choices=[(1,'CLR [Children play a game on a laptop/ tablet at the lab/ clinic supervised by experimenters and/or parents]'),
                 (2,'PNLRA [Children play a game on a laptop/ tablet at home supervised by parents]'),
                 (3,'NRWRA [Children play an online application at home by themselves when they feel like it]'),
                 (4,'No intervention component')],
        default=4,
        validators=[validators.InputRequired()])
    TQ8 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')
    
    return (INTERTITLE,Q8,TQ8)

class NumexpForm(Form):
    Num_exp = IntegerField(
        label='1) Insert number of experiments',
        default=1,
        validators=[validators.InputRequired(),validators.NumberRange(min=1, max=3, message='Up to 3')])

    Intervention_switcher = RadioField(
        '2) Is there an intervention component?',
        [validators.DataRequired()],
        choices=[('Yes', 'Yes, I have an intervention component'), ('No', 'No, I do not have an intervention')], default='No' )

class formOneTaskNoInt(Form):
    Q1a = TextField(
        label='1a) What behavior are you trying to observe?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=45)])
    
    Q1b = TextField(
        label='1b) What is the context you aim to generalize to?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=150)])

    Q2 = RadioField(
        label='2. ...how your sample reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Convenience sample, such as undergraduate students at a university]'),
                 (2,'PNLRA [Community-based recruitment]'),
                 (3,'NRWRA  [A large, nationally representative sample of school districts in a city]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextAreaField(label='Please justify your answer below.', default='No comment')
    # TASK Q1
    Q3 = RadioField(
        label='3. ...how your testing site reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Lab/ clinical testing room]'),
                 (2,'PNLRA [Lab set up to look like a classroom]'),
                 (3,'NRWRA [Classroom with little/no experimenter presence and interference into teaching activities]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ3 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q4 = RadioField(
        label='4. ... how your task reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                 (2,'PNLRA [Test of memory after viewing a movie]'),
                 (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ4 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q5 = RadioField(
        label='5. ... how your stimuli reflect that context?',
        coerce=int,
        choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                 (2,'PNLRA [Dynamic stimuli, like dynamic faces on video] '),
                 (3,'NRWRA [Fully naturalistically sampled stimuli: people during social interaction]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q6 = RadioField(
        label='6. ...how your measures reflect that behavior?',
        coerce=int,
        choices=[(1,'CLR [Well-researched brain correlates of a specific cognitive process in typical conditions]'),
                 (2,'PNLRA [Canonical brain correlates in non-traditional laboratory settings and/or using more portable tools]'),
                 (3,'NRWRA [Portable imaging tools in external environments to test for canonical correlates of cognitive processes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q7 = RadioField(
        label='7. Are non-research stakeholders involved? ( teachers, caretaker, institutions, clinicians)',
        coerce=int,
        choices=[(1,'CLR [Stakeholders only facilitate access to the sample]'),
                 (2,'PNLRA [Stakeholders involved in conception OR interpretation/writing up the results]'),
                 (3,'NRWRA [Involvement in conception of project AND interpretation/writing up the results]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')
 

        #########################################################################################################################################################
       
class formTwoTaskNoInt(Form):
    Q1a = TextField(
        label='1a) What behavior are you trying to observe?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=45)])
    
    Q1b = TextField(
        label='1b) What is the context you aim to generalize to?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=150)])

    Q2 = RadioField(
        label='2. ...how your sample reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Convenience sample, such as undergraduate students at a university]'),
                 (2,'PNLRA [Community-based recruitment]'),
                 (3,'NRWRA  [A large, nationally representative sample of school districts in a city]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextAreaField(label='Please justify your answer below.', default='No comment')
    # TASK Q1
    TASK1 = TextField(label='Would you like to give your first task a name?',default='No title') 

    Q3 = RadioField(
        label='3. ...how your testing site reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Lab/ clinical testing room]'),
                 (2,'PNLRA [Lab set up to look like a classroom]'),
                 (3,'NRWRA [Classroom with little/no experimenter presence and interference into teaching activities]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ3 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q4 = RadioField(
        label='4. ... how your task reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                 (2,'PNLRA [Test of memory after viewing a movie]'),
                 (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ4 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q5 = RadioField(
        label='5. ... how your stimuli reflect that context?',
        coerce=int,
        choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                 (2,'PNLRA [Dynamic stimuli, like dynamic faces on video] '),
                 (3,'NRWRA [Fully naturalistically sampled stimuli: people during social interaction]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q6 = RadioField(
        label='6. ...how your measures reflect that behavior?',
        coerce=int,
        choices=[(1,'CLR [Well-researched brain correlates of a specific cognitive process in typical conditions]'),
                 (2,'PNLRA [Canonical brain correlates in non-traditional laboratory settings and/or using more portable tools]'),
                 (3,'NRWRA [Portable imaging tools in external environments to test for canonical correlates of cognitive processes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q7 = RadioField(
        label='7. Are non-research stakeholders involved? ( teachers, caretaker, institutions, clinicians)',
        coerce=int,
        choices=[(1,'CLR [Stakeholders only facilitate access to the sample]'),
                 (2,'PNLRA [Stakeholders involved in conception OR interpretation/writing up the results]'),
                 (3,'NRWRA [Involvement in conception of project AND interpretation/writing up the results]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')
 
    TASK2,Q3b,TQ3b,Q4b,TQ4b,Q5b,TQ5b,Q6b,TQ6b =  indivQ(2)
        
        #########################################################################################################################################################
       
class formThreeTaskNoInt(Form):
    Q1a = TextField(
        label='1a) What behavior are you trying to observe?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=45)])
    
    Q1b = TextField(
        label='1b) What is the context you aim to generalize to?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=150)])

    Q2 = RadioField(
        label='2. ...how your sample reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Convenience sample, such as undergraduate students at a university]'),
                 (2,'PNLRA [Community-based recruitment]'),
                 (3,'NRWRA  [A large, nationally representative sample of school districts in a city]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextAreaField(label='Please justify your answer below.', default='No comment')
    # TASK Q1
    TASK1 = TextField(label='Would you like to give your first task a name?',default='No title') 
    Q3 = RadioField(
        label='3. ...how your testing site reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Lab/ clinical testing room]'),
                 (2,'PNLRA [Lab set up to look like a classroom]'),
                 (3,'NRWRA [Classroom with little/no experimenter presence and interference into teaching activities]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ3 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q4 = RadioField(
        label='4. ... how your task reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                 (2,'PNLRA [Test of memory after viewing a movie]'),
                 (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ4 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q5 = RadioField(
        label='5. ... how your stimuli reflect that context?',
        coerce=int,
        choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                 (2,'PNLRA [Dynamic stimuli, like dynamic faces on video] '),
                 (3,'NRWRA [Fully naturalistically sampled stimuli: people during social interaction]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q6 = RadioField(
        label='6. ...how your measures reflect that behavior?',
        coerce=int,
        choices=[(1,'CLR [Well-researched brain correlates of a specific cognitive process in typical conditions]'),
                 (2,'PNLRA [Canonical brain correlates in non-traditional laboratory settings and/or using more portable tools]'),
                 (3,'NRWRA [Portable imaging tools in external environments to test for canonical correlates of cognitive processes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q7 = RadioField(
        label='7. Are non-research stakeholders involved? ( teachers, caretaker, institutions, clinicians)',
        coerce=int,
        choices=[(1,'CLR [Stakeholders only facilitate access to the sample]'),
                 (2,'PNLRA [Stakeholders involved in conception OR interpretation/writing up the results]'),
                 (3,'NRWRA [Involvement in conception of project AND interpretation/writing up the results]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')
 
    TQF = TextAreaField(
        label='8. Please indicate in which category (CLR, PNLRA, and NRWRA) you see your research fits best and state the reasons.',
        default='No comment')
    TASK2,Q3b,TQ3b,Q4b,TQ4b,Q5b,TQ5b,Q6b,TQ6b =  indivQ(2)
    TASK3,Q3c,TQ3c,Q4c,TQ4c,Q5c,TQ5c,Q6c,TQ6c =  indivQ(3)
   
        #########################################################################################################################################################
       
class formOneTaskYesInt(Form):
    Q1a = TextField(
        label='1a) What behavior are you trying to observe?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=45)])
    
    Q1b = TextField(
        label='1b) What is the context you aim to generalize to?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=150)])

    Q2 = RadioField(
        label='2. ...how your sample reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Convenience sample, such as undergraduate students at a university]'),
                 (2,'PNLRA [Community-based recruitment]'),
                 (3,'NRWRA  [A large, nationally representative sample of school districts in a city]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextAreaField(label='Please justify your answer below.', default='No comment')
    # TASK Q1
    Q3 = RadioField(
        label='3. ...how your testing site reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Lab/ clinical testing room]'),
                 (2,'PNLRA [Lab set up to look like a classroom]'),
                 (3,'NRWRA [Classroom with little/no experimenter presence and interference into teaching activities]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ3 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q4 = RadioField(
        label='4. ... how your task reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                 (2,'PNLRA [Test of memory after viewing a movie]'),
                 (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ4 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q5 = RadioField(
        label='5. ... how your stimuli reflect that context?',
        coerce=int,
        choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                 (2,'PNLRA [Dynamic stimuli, like dynamic faces on video] '),
                 (3,'NRWRA [Fully naturalistically sampled stimuli: people during social interaction]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q6 = RadioField(
        label='6. ...how your measures reflect that behavior?',
        coerce=int,
        choices=[(1,'CLR [Well-researched brain correlates of a specific cognitive process in typical conditions]'),
                 (2,'PNLRA [Canonical brain correlates in non-traditional laboratory settings and/or using more portable tools]'),
                 (3,'NRWRA [Portable imaging tools in external environments to test for canonical correlates of cognitive processes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q7 = RadioField(
        label='7. Are non-research stakeholders involved? ( teachers, caretaker, institutions, clinicians)',
        coerce=int,
        choices=[(1,'CLR [Stakeholders only facilitate access to the sample]'),
                 (2,'PNLRA [Stakeholders involved in conception OR interpretation/writing up the results]'),
                 (3,'NRWRA [Involvement in conception of project AND interpretation/writing up the results]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    INTERTITLE,Q8,TQ8 = interventionQ()
        #########################################################################################################################################################
       
class formTwoTaskYesInt(Form):
    Q1a = TextField(
        label='1a) What behavior are you trying to observe?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=45)])
    
    Q1b = TextField(
        label='1b) What is the context you aim to generalize to?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=150)])

    Q2 = RadioField(
        label='2. ...how your sample reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Convenience sample, such as undergraduate students at a university]'),
                 (2,'PNLRA [Community-based recruitment]'),
                 (3,'NRWRA  [A large, nationally representative sample of school districts in a city]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextAreaField(label='Please justify your answer below.', default='No comment')
    # TASK Q1
    TASK1 = TextField(label='Would you like to give your first task a name?',default='No title') 
    Q3 = RadioField(
        label='3. ...how your testing site reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Lab/ clinical testing room]'),
                 (2,'PNLRA [Lab set up to look like a classroom]'),
                 (3,'NRWRA [Classroom with little/no experimenter presence and interference into teaching activities]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ3 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q4 = RadioField(
        label='4. ... how your task reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                 (2,'PNLRA [Test of memory after viewing a movie]'),
                 (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ4 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q5 = RadioField(
        label='5. ... how your stimuli reflect that context?',
        coerce=int,
        choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                 (2,'PNLRA [Dynamic stimuli, like dynamic faces on video] '),
                 (3,'NRWRA [Fully naturalistically sampled stimuli: people during social interaction]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextAreaField(label='Please justify your answer below.',default='No comment')

    Q6 = RadioField(
        label='6. ...how your measures reflect that behavior?',
        coerce=int,
        choices=[(1,'CLR [Well-researched brain correlates of a specific cognitive process in typical conditions]'),
                 (2,'PNLRA [Canonical brain correlates in non-traditional laboratory settings and/or using more portable tools]'),
                 (3,'NRWRA [Portable imaging tools in external environments to test for canonical correlates of cognitive processes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextAreaField(label='Please justify your answer below.', default='No comment')

    Q7 = RadioField(
        label='7. Are non-research stakeholders involved? ( teachers, caretaker, institutions, clinicians)',
        coerce=int,
        choices=[(1,'CLR [Stakeholders only facilitate access to the sample]'),
                 (2,'PNLRA [Stakeholders involved in conception OR interpretation/writing up the results]'),
                 (3,'NRWRA [Involvement in conception of project AND interpretation/writing up the results]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextAreaField(
        label='Please justify your answer below.',
        default='No comment')

    INTERTITLE,Q8,TQ8 = interventionQ()
    TASK2,Q3b,TQ3b,Q4b,TQ4b,Q5b,TQ5b,Q6b,TQ6b =  indivQ(2)
        
        #########################################################################################################################################################
       
class formThreeTaskYesInt(Form):
    Q1a = TextField(
        label='1a) What behavior are you trying to observe?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=45)])
    
    Q1b = TextField(
        label='1b) What is the context you aim to generalize to?',
        default='...',
        validators=[validators.InputRequired(),validators.Length(max=150)])

    Q2 = RadioField(
        label='2. ...how your sample reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Convenience sample, such as undergraduate students at a university]'),
                 (2,'PNLRA [Community-based recruitment]'),
                 (3,'NRWRA  [A large, nationally representative sample of school districts in a city]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ2 = TextField(label='Please justify your answer below.', default='No comment')
    # TASK Q1
    TASK1 = TextField(label='Would you like to give your first task a name?',default='No title') 
    Q3 = RadioField(
        label='3. ...how your testing site reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Lab/ clinical testing room]'),
                 (2,'PNLRA [Lab set up to look like a classroom]'),
                 (3,'NRWRA [Classroom with little/no experimenter presence and interference into teaching activities]')],
        default=1,
        validators=[validators.InputRequired()])   
    TQ3 = TextField(label='Please justify your answer below.',default='No comment')

    Q4 = RadioField(
        label='4. ... how your task reflects that context?',
        coerce=int,
        choices=[(1,'CLR [Working memory task for shapes presented on a screen]'),
                 (2,'PNLRA [Test of memory after viewing a movie]'),
                 (3,'NRWRA [Test of memory of an interaction after a prolonged delay that involved other activities]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ4 = TextField(label='Please justify your answer below.', default='No comment')

    Q5 = RadioField(
        label='5. ... how your stimuli reflect that context?',
        coerce=int,
        choices=[(1,'CLR [Static stimuli, typical for perceptual/cognitive studies, like face images]'),
                 (2,'PNLRA [Dynamic stimuli, like dynamic faces on video] '),
                 (3,'NRWRA [Fully naturalistically sampled stimuli: people during social interaction]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ5 = TextField(label='Please justify your answer below.',default='No comment')

    Q6 = RadioField(
        label='6. ...how your measures reflect that behavior?',
        coerce=int,
        choices=[(1,'CLR [Well-researched brain correlates of a specific cognitive process in typical conditions]'),
                 (2,'PNLRA [Canonical brain correlates in non-traditional laboratory settings and/or using more portable tools]'),
                 (3,'NRWRA [Portable imaging tools in external environments to test for canonical correlates of cognitive processes]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ6 = TextField(label='Please justify your answer below.', default='No comment')

    Q7 = RadioField(
        label='7. Are non-research stakeholders involved? ( teachers, caretaker, institutions, clinicians)',
        coerce=int,
        choices=[(1,'CLR [Stakeholders only facilitate access to the sample]'),
                 (2,'PNLRA [Stakeholders involved in conception OR interpretation/writing up the results]'),
                 (3,'NRWRA [Involvement in conception of project AND interpretation/writing up the results]')],
        default=1,
        validators=[validators.InputRequired()])
    TQ7 = TextField(
        label='Please justify your answer below.',
        default='No comment')
 

    INTERTITLE,Q8,TQ8 = interventionQ()
    TASK2,Q3b,TQ3b,Q4b,TQ4b,Q5b,TQ5b,Q6b,TQ6b =  indivQ(2)
    TASK3,Q3c,TQ3c,Q4c,TQ4c,Q5c,TQ5c,Q6c,TQ6c =  indivQ(3)
   

    
