#!/usr/bin/env python

"""
A feature extractor for chunking.
Copyright 2010,2011 Naoaki Okazaki.
"""

# Separator of field values.
separator = ' '

# Field names of the input data.
fields = 'w beg end hasno allno four1 four2 four3 four4 four5 prev_from prev_by prev_and dict_brand dict_color dict_model_id dict_headphone_jack dict_cord_length dict_wired_wireless dict_headset_design dict_headset_type y'

# Attribute templates.
templates = (
    (('w', -2), ),
    (('w', -1), ),
    (('w',  0), ),
    (('w',  1), ),
    (('w',  2), ),
    (('beg',  0), ),
    (('end',  0), ),
    (('hasno',  0), ),
    (('allno',  0), ),
    (('four1',  0), ),
    (('four2',  0), ),
    (('four3',  0), ),
    (('four4',  0), ),
    (('four1',  -1), ),
    (('four2',  -1), ),
    (('four3',  -1), ),
    (('four4',  -1), ),
    (('four1',  1), ),
    (('four2',  1), ),
    (('four3',  1), ),
    (('four4',  1), ),
    (('prev_from',  0), ),
    (('prev_by',  0), ),
    (('prev_and',  0), ),
    (('dict_brand',  0), ),
    (('dict_color',  0), ),
    (('dict_model_id',  0), ),
    (('dict_headphone_jack',  0), ),
    (('dict_wired_wireless',  0), ),
    (('dict_cord_length',  0), ),
    (('dict_headset_type',  0), ),
    (('dict_headset_design',  0), ),
    )


import crfutils

def feature_extractor(X):
    # Apply attribute templates to obtain features (in fact, attributes)
    crfutils.apply_templates(X, templates)
    if X:
	# Append BOS and EOS features manually
        X[0]['F'].append('__BOS__')     # BOS feature
        X[-1]['F'].append('__EOS__')    # EOS feature

if __name__ == '__main__':
    crfutils.main(feature_extractor, fields=fields, sep=separator)
