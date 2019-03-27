
# coding: utf-8

# In[331]:


get_ipython().run_line_magic('pylab', 'inline')


# In[329]:


class Slide():
    def __init__(self, photos, tags):
        self.photos = photos
        self.tags = tags
    def __repr__(self):
        return 'Tags: {} (IDS: {})'.format(self.tags, ", ".join([str(x.id) for x in self.photos]))


# In[330]:


class Photo():
    def __init__(self, mode, tags, id):
        self.mode = mode
        self.tags = tags
        self.id = id
    def __repr__(self): return "ID: {} Mode: {} Tags: {}".format(self.id, self.mode, self.tags)


# In[210]:


def readlines(file):
    with open(file) as fp:
        lines = fp.readlines()
        return [x.rstrip() for x in lines][1:]


# In[266]:


def lineToPhoto(string, i):
    mode = string[0:1]
    tagCount = string[2:3]
    tags = string[4:].split(' ')
    return Photo(mode, tags, i)


# In[265]:


def parseToPhotos(lines):
    return [lineToPhoto(lines[i], i) for i in range(len(lines))]


# In[332]:


def getMaxIndex(A):
    n = len(A)
    q = np.argmax(A)
    row = q // n
    col = q - row*n
    return (row, col)


# In[333]:


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


# In[334]:


def createSlidesFromVerticalImages(verticals):
    
    slides = []
    A = createVertMatrix(verticals)
    k = len(verticals) // 2
    
    for _ in range(k):
        y, x = getMaxIndex(A)
        photos = [verticals[x], verticals[y]]
        A[x,y] = A[y,x] = 0
        tags = list(set(photos[0].tags + photos[1].tags))
        slide = Slide(photos, tags)
        slides.append(slide)
        
    return slides    


# In[337]:


def fileToSlides(filepath):
    lines = readlines(filepath)
    photos = parseToPhotos(lines)
    verticals = [x for x in photos if x.mode == 'V']
    horizontals = [x for x in photos if x.mode == 'H']
    return createSlidesFromVerticalImages(verticals) + [Slide([x], x.tags) for x in horizontals]


# In[391]:


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


# In[397]:


def transitionMatrixToSlideshow(A, slides):
    slideshow = []
    (q,r) = getMaxIndex(A)
    slideshow.append(slides[q])
    slideshow.append(slides[r])
    A[q,r] = A[r,q] = -1
    prevIndex = r

    while len(slideshow) < len(slides):  
        r, c = getMaxIndex(A[prevIndex:prevIndex+1,:]) 
        if slides[r] not in slideshow:
            slideshow.append(slides[r])
            prevIndex = r
        elif slides[c] not in slideshow:
            slideshow.append(slides[c])
            prevIndex = c

        A[r,c] = A[c,r] = -1
    return slideshow


# In[398]:


def fileToSlideshow(file):
    slides = fileToSlides(file)
    A = transitionMatrix(slides)
    return transitionMatrixToSlideshow(A, slides)


# In[399]:


s = fileToSlideshow('a_example.txt')
s


# In[416]:


s


# In[446]:


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


# In[448]:


sToFile(s, 'A.txt')

