
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


class Slide():
    def __init__(self, photos, tags):
        self.photos = photos
        self.tags = tags
    def __repr__(self):
        return 'Tags: {} (IDS: {})'.format(self.tags, ", ".join([str(x.id) for x in self.photos]))


# In[3]:


class Photo():
    def __init__(self, mode, tags, id):
        self.mode = mode
        self.tags = tags
        self.id = id
    def __repr__(self): return "ID: {} Mode: {} Tags: {}".format(self.id, self.mode, self.tags)


# In[4]:


def readlines(file):
    with open(file) as fp:
        lines = fp.readlines()
        return [x.rstrip() for x in lines][1:]


# In[5]:


def lineToPhoto(string, i):
    mode = string[0:1]
    tagCount = string[2:3]
    tags = string[4:].split(' ')
    return Photo(mode, tags, i)


# In[6]:


def parseToPhotos(lines):
    return [lineToPhoto(lines[i], i) for i in range(len(lines))]


# In[7]:


def getMaxIndex(A):
    n = len(A)
    q = np.argmax(A)
    row = q // n
    col = q - row*n
    return (row, col)


# In[8]:


def createVertMatrix(verticals):
    
    n = len(verticals)
    A = np.zeros(n*n).reshape((n,n))
    
    for i in range(n):
        for j in range(n):
            if i is j: continue
            photoA = verticals[i]
            photoB = verticals[j]
            tags = set(photoA.tags + photoB.tags)
            A[i,j] = max(len(tags), A[i,j])
    
    return A


# In[71]:


def createSlidesFromVerticalImages(verticals):
    
    slides = []
    photosInSlides = []
    A = createVertMatrix(verticals)
    k = len(verticals) // 2
    
    
    
    
    
    for _ in range(k):
        y, x = getMaxIndex(A)
        
        if verticals[x] not in photosInSlides and verticals[y] not in photosInSlides:
            photos = [verticals[x], verticals[y]]        
            photosInSlides.append(verticals[x])
            photosInSlides.append(verticals[y])        
            tags = list(set(photos[0].tags + photos[1].tags))
            slide = Slide(photos, tags)
            slides.append(slide)        
        A[x,y] = A[y,x] = -1
        
        
    return slides    


# In[72]:


def fileToSlides(filepath):
    lines = readlines(filepath)
    photos = parseToPhotos(lines)
    verticals = [x for x in photos if x.mode == 'V']
    horizontals = [x for x in photos if x.mode == 'H']
    return createSlidesFromVerticalImages(verticals) + [Slide([x], x.tags) for x in horizontals]


# In[73]:


def transitionMatrix(slides):
    n = len(slides)
    A = np.zeros(n*n).reshape((n,n))

    for i in range(n):
        for j in range(n):
            if i is j: continue
            slideA = slides[i]
            slideB = slides[j]
            tags = set(slideA.tags).intersection(set(slideB.tags))
            A[i,j] = max(len(tags), A[i,j])
            
    return A


# In[74]:


def transitionMatrixToSlideshow(A, slides):
    slideshow = []
    (r, c) = getMaxIndex(A)
    slideshow.append(slides[r])
    slideshow.append(slides[c])
    A[r,c] = A[c,r] = -1
    prevIndex = r
    
    while len(slideshow) < len(slides):  
        c = np.argmax(A[prevIndex:prevIndex+1,:])
                  
        if not slides[c] in slideshow: 
            slideshow.append(slides[c])            
            prevIndex = c
            
        A[prevIndex,c] = A[c,prevIndex] = -1
        
    return slideshow


# In[75]:


def sToFile(s, file):
    result = []
    result.append(len(s))
    for r in s:
        res = ""
        for p in r.photos:
            res += str(p.id) + ' '
            
        result.append(res.rstrip())
        
    f = open(file, "w")
    f.write("\n".join([str(x) for x in result]))
    f.close()


# In[76]:


def fileToSlideshow(file, outfile):
    slides = fileToSlides(file)
    A = transitionMatrix(slides)
    S = transitionMatrixToSlideshow(A, slides)
    sToFile(S, outfile)


# In[77]:


s = fileToSlideshow('c_memorable_moments.txt', 'C.txt')

