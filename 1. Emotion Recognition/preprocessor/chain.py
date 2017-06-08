from preprocessor.processor.impl.scale import ScaleProcessor


# Class describes sequence of processor, which should be applied to the image
class ProcessorChain:
    # Method sets sequence of processors
    def __init__(self):
        self.chain = list()
        self.chain.append(ScaleProcessor())
        # add more processors here

    # main method for running pre process actions
    def run(self, image):
        for p in self.chain:
            p.process(image)
        return image
