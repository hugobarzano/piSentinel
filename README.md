# piSentinel

Face learning and searching example


### Usage

        Usage::
            python3  piSentinel.py -h shows this help()
            python3  piSentinel.py -t <face_name>  to teach your face to piSentinel
            python3  piSentinel.py -s              to make piSentinel search some known faces
            
        Info:: 
            Press Key 'q' to exit camera frame and save data learning
            
### Dependencies

   python3 [Download](https://www.python.org/downloads/)
   
         virtualenv <env_name>
         source <env_name>/bin/activate
         pip3 install -r requirements.txt
         
### Example

Let's go to teach Hugo's face to piSentinel:

    python3  piSentinel.py -t Hugo
    
 ![Hugo](https://github.com/hugobarzano/piSentinel/blob/master/img/doc_hugo.png "Hugo")
 
 
When cam start recording and recognize the face press Q to make piSentinel to learn the face.
Learned faces will be saved inside img/ folder.
 
Let's go to search some face:
 
    python3 piSentinel.py -s  
 
 
Faces known by piSentinel will be labeled with their name:

  ![Crazzy Hugo](https://github.com/hugobarzano/piSentinel/blob/master/img/doc_hugo2.png "Crazzy Hugo")

 
Faces not known by piSentinel will be labeled with unknown

  ![Jim Morrison](https://github.com/hugobarzano/piSentinel/blob/master/img/doc_jim.png "Jim Morrison")



