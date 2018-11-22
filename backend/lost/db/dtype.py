'''Defines all possible types in lost
'''

__author__ = 'Jonas Jaeger'

class RawFile():
    '''Type of this RawFile.

    Attributes:
        VIDEO (1): A video file.
        IMAGESET (2): A folder containing image files.
        FILE (3): Generic File.
        URL (4): URL.
    '''
    VIDEO = 1
    IMAGESET = 2
    FILE = 3
    URL = 4

class AnnoTask():
    '''The Type of an AnnotationTask.

    The AnnoTaskType indicates in which annotation tool should be used.

    Attributes:
        MIA (1): MultiImageAnnotation Tool. 
        SIA (2): SingleImageAnnotationTool
    '''
    MIA = 1
    SIA = 2

class Datasource():
    '''Type of a Datasource

    Attributes:
       DATASET (1): A Dataset.
       MODEL_LEAF (2): A ModelLeaf.
       RAW_FILE (3): A RawFile.
       PIPE_ELEMENT (4): A PipeElement (for e.g. Script)
    '''
    DATASET = 1
    MODEL_LEAF = 2
    RAW_FILE = 3
    PIPE_ELEMENT = 4

class PipeElement():
    '''Type of an PipeElement.

    Attributes:
        SCRIPT (0): A script.
        ANNO_TASK (1): An AnnoTask.
        DATASOURCE (2): A datasource, that can be an video and imageset or a
            virtual dataset.
        VISUALIZATION (3): This element will visualize data.
        DATA_EXPORT (4): Represants an arbitrary file that can be downloaded.
        LOOP (5): A loop element that acts like a while loop.
    '''
    SCRIPT = 0
    ANNO_TASK = 1
    DATASOURCE = 2
    VISUALIZATION = 3
    DATA_EXPORT = 4
    LOOP = 5

class Label():
    '''Type of a label.

    Attributes:
        IMG_ANNO (1): An ImageAnnotation.
        TWO_D_ANNO (2): A TwoDAnnotation.
    '''
    IMG_ANNO = 1
    TWO_D_ANNO = 2

class VisualOutput():
    '''Type of a VisualOutput

    Attributes:
        IMAGE (0): A output image that was generated by a script. Could be a
            diagram created with matplotlib for example.
        HTML (1): HTML output that will be used to display information for a
            PipelineElement.
    '''
    IMAGE = 0
    HTML = 1

class TwoDAnno():
    '''Type of a TwoDAnno

    Attributes:
       BBOX (1): A BBox.
       POLYGON (2): A Polygon.
       POINT (3): A Point.
       LINE (4): A Line.
       CIRCLE (5): A Circle.

    '''
    BBOX = 1
    POLYGON = 2
    POINT = 3
    LINE = 4
    CIRCLE = 5

    TYPE_TO_STR = {
        1:'bbox', 
        2:'polygon',
        3:'point',
        4:'line',
        5:'circle'
    }

    STR_TO_TYPE = {v:k for (k,v) in TYPE_TO_STR.items()}