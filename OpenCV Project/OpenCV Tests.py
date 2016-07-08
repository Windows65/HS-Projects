from matplotlib import pyplot as plt
import numpy as np
import subprocess
import colorsys
import sys
import cv2
def cls():
    print "\n"*45
    subprocess.call("cls", shell=True)

def showBlue():
    try:
        print "[Notice] | Initilizing Blue Extraction..."
        cap = cv2.VideoCapture(0)
        green = np.uint8([[[0,255,0 ]]])
        hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
        print "[Notice] | Starting Blue Extraction..."
        print "/n [Notice] | Press CTRL + C to properly exit."
        while(1):
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([50,50,50])
            upper_blue = np.array([130,255,255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            res = cv2.bitwise_and(frame,frame, mask= mask)
            cv2.imshow('Origional',frame)
            cv2.imshow('After Processing',res)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        print "[Notice] | Blue Extraction Complete!"
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        toDo = raw_input("-"*45+"\n\n[Notice] | Script Paused...\n>" + "---"*13 + "<\n> Main Menu-------------(1)" + "\n> Continue Script-------(Any Other Key)\n>" + "---"*13 + "<\n\n> ")
        if "1" in toDo:
            cv2.destroyAllWindows()
            main()
        else:
            pass
    except Exception,e:
        if "something@R" in str(e):
            print "[Error] | Something Happaned."
        else:
            raw_input("[Error] | > " + str(e))
            cv2.destroyAllWindows()
            main()









def detectCorners():
    try:
        print "[Notice] | Initilizing Corner Detection..."
        cap = cv2.VideoCapture(0)
        print "[Notice] | Starting Corner Detection..."
        print "/n [Notice] | Press CTRL + C to properly exit."
        while(1):
            _, frame = cap.read()
            img = frame
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            gray = np.float32(gray)
            dst = cv2.cornerHarris(gray,2,3,0.04)
            dst = cv2.dilate(dst,None)
            img[dst>0.01*dst.max()]=[0,0,255]
            cv2.imshow('Corner Tracking',img)
            
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        print "[Notice] | Corner Detection Complete!"
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        toDo = raw_input("-"*45+"\n\n[Notice] | Script Paused...\n>" + "---"*13 + "<\n> Main Menu-------------(1)" + "\n> Continue Script-------(Any Other Key)\n>" + "---"*13 + "<\n\n> ")
        if "1" in toDo:
            cv2.destroyAllWindows()
            main()
        else:
            pass
    except Exception,e:
        if "something@R" in str(e):
            print "[Error] | Something Happaned."
        else:
            raw_input("[Error] | > " + str(e))
            cv2.destroyAllWindows()
            main()




def objectDetection():
    toDetect = []
    eyes = []
    prev = 0
    choice = raw_input("""
What Object Would You Like To Detect?
>------------------------------------------<
| Faces:--------------------------(1)
| Face+Eyes:----------------------(2)
| Full Body:----------------------(3)
| Smile:--------------------------(4)
| Cat Face:-----------------------(5)
| Custom:-------------------------(6)
>------------------------------------------<

> """)
    if "1" in choice:
        toDetect.append("haarcascade_frontalface_default.xml")
    elif "2" in choice:
        toDetect.append("haarcascade_frontalface_default.xml")
        toDetect.append("haarcascade_eye.xml")
    elif "3" in choice:
        toDetect.append("haarcascade_fullbody.xml")
    elif "4" in choice:
        toDetect.append("haarcascade_smile.xml")
    elif "5" in choice:
        toDetect.append("haarcascade_frontalcatface.xml")
    elif "6" in choice:
        toDetect.append(raw_input("Input the name of the detction file (Has to be in same directory)\n" + "-----"*14 + "\n> "))
        if ".xml" in toDetect[0]:
            pass
        else:
            print "[.xml] File Not Detected..\nYour Input: [{0}]\n".format(toDetect[0])
            cls()
            objectDetection()
    else:
        raw_input("\n\n\nUnable to understand your input\n> ")
        cls()
        objectDetection()


    try:
        print "[Notice] | Initilizing Blue Extraction..."
        cap = cv2.VideoCapture(0)
        print "[Notice] | Starting Blue Extraction..."
        faceCascade = cv2.CascadeClassifier(toDetect[0])
        if "haarcascade_eye.xml" in toDetect:
            eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        while(1):
            _, image = cap.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
            )
            if "haarcascade_eye.xml" in toDetect:
                eyes = eyeCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                )
            if len(faces)+len(eyes) != prev:
                print "[Found] | Faces = ({0}) | Eyes = ({1})".format(len(faces),len(eyes))
                prev = len(faces)+len(eyes)
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if "haarcascade_eye.xml" in toDetect:
                for (x, y, w, h) in eyes:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("Objects Found", image)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        print "[Notice] | Blue Extraction Complete!"
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        toDo = raw_input("-"*45+"\n\n[Notice] | Script Paused...\n>" + "---"*13 + "<\n> Main Menu-------------(1)" + "\n> Continue Script-------(Any Other Key)\n>" + "---"*13 + "<\n\n> ")
        if "1" in toDo:
            cv2.destroyAllWindows()
            main()
        else:
            pass
    except Exception,e:
        if "something@R" in str(e):
            print "[Error] | Something Happaned."
        else:
            raw_input("[Error] | > " + str(e))
            cv2.destroyAllWindows()
            main()









def motionTracking():
    try:
        cap = cv2.VideoCapture(0)

        # take first frame of the video
        ret,frame = cap.read()

        # setup initial location of window
        r,h,c,w = 250,90,400,125  # simply hardcoded the values
        track_window = (c,r,w,h)

        # set up the ROI for tracking
        roi = frame[r:r+h, c:c+w]
        hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

        # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

        while(1):
            ret ,frame = cap.read()

            if ret == True:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

                # apply meanshift to get the new location
                ret, track_window = cv2.CamShift(dst, track_window, term_crit)

                # Draw it on image
                pts = cv2.boxPoints(ret)
                pts = np.int0(pts)
                img2 = cv2.polylines(frame,[pts],True, 255,2)
                cv2.imshow('img2',img2)

                k = cv2.waitKey(60) & 0xff
                if k == 27:
                    break
                else:
                    cv2.imwrite(chr(k)+".jpg",img2)
            else:
                print "Loop Broken..."
                break

        cv2.destroyAllWindows()
        cap.release()
    except KeyboardInterrupt:
        toDo = raw_input("-"*45+"\n\n[Notice] | Script Paused...\n>" + "---"*13 + "<\n> Main Menu-------------(1)" + "\n> Continue Script-------(Any Other Key)\n>" + "---"*13 + "<\n\n> ")
        if "1" in toDo:
            cv2.destroyAllWindows()
            main()
        else:
            pass
    except Exception,e:
        if "something@R" in str(e):
            print "[Error] | Something Happaned."
        else:
            raw_input("[Error] | > " + str(e))
            cv2.destroyAllWindows()
            main()





def opticalFlow(showGlich, showHSV):
    try:
        def draw_flow(img, flow, step=16):
            h, w = img.shape[:2]
            y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1)
            fx, fy = flow[y,x].T
            lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
            lines = np.int32(lines + 0.5)
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.polylines(vis, lines, 0, (0, 255, 0))
            for (x1, y1), (x2, y2) in lines:
                cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
            return vis
        def draw_hsv(flow):
            h, w = flow.shape[:2]
            fx, fy = flow[:,:,0], flow[:,:,1]
            ang = np.arctan2(fy, fx) + np.pi
            v = np.sqrt(fx*fx+fy*fy)
            hsv = np.zeros((h, w, 3), np.uint8)
            hsv[...,0] = ang*(180/np.pi/2)
            hsv[...,1] = 255
            hsv[...,2] = np.minimum(v*4, 255)
            bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            return bgr
        def warp_flow(img, flow):
            h, w = flow.shape[:2]
            flow = -flow
            flow[:,:,0] += np.arange(w)
            flow[:,:,1] += np.arange(h)[:,np.newaxis]
            res = cv2.remap(img, flow, None, cv2.INTER_LINEAR)
            return res
        
        try:
            fn = sys.argv[1]
        except:
            fn = 0

        cam = cv2.VideoCapture(0)
        ret, prev = cam.read()
        prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        show_hsv = showHSV
        show_glitch = showGlich
        cur_glitch = prev.copy()

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            prevgray = gray

            cv2.imshow('flow', draw_flow(gray, flow))
            if show_hsv:
                cv2.imshow('flow HSV', draw_hsv(flow))
            if show_glitch:
                cur_glitch = warp_flow(cur_glitch, flow)
                cv2.imshow('glitch', cur_glitch)

            ch = 0xFF & cv2.waitKey(5)
            if ch == 27:
                break
            if ch == ord('1'):
                show_hsv = not show_hsv
                print 'HSV flow visualization is', ['off', 'on'][show_hsv]
            if ch == ord('2'):
                show_glitch = not show_glitch
                if show_glitch:
                    cur_glitch = img.copy()
                print 'glitch is', ['off', 'on'][show_glitch]


    except KeyboardInterrupt:
        toDo = raw_input("-"*45+"\n\n[Notice] | Script Paused...\n>" + "---"*13 + "<\n> Main Menu-------------(1)" + "\n> Continue Script-------(Any Other Key)\n>" + "---"*13 + "<\n\n> ")
        if "1" in toDo:
            cv2.destroyAllWindows()
            main()
        else:
            pass
    except Exception,e:
        if "something@R" in str(e):
            print "[Error] | Something Happaned."
        else:
            raw_input("[Error] | > " + str(e))
            cv2.destroyAllWindows()
            main()








def facialRecognition():
    try:
        img1 = cv2.VideoCapture(0)
        img2 = cv2.imread("me.jpg",0)

        # Initiate SIFT detector
        sift = cv2.SIFT()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1,None)
        kp2, des2 = sift.detectAndCompute(img2,None)

        # FLANN parameters
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary

        flann = cv2.FlannBasedMatcher(index_params,search_params)

        matches = flann.knnMatch(des1,des2,k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0,0] for i in xrange(len(matches))]

        # ratio test as per Lowe's paper
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.7*n.distance:
                matchesMask[i]=[1,0]

        draw_params = dict(matchColor = (0,255,0),
                           singlePointColor = (255,0,0),
                           matchesMask = matchesMask,
                           flags = 0)

        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

        plt.imshow(img3,),plt.show()

    except KeyboardInterrupt:
        toDo = raw_input("-"*45+"\n\n[Notice] | Script Paused...\n>" + "---"*13 + "<\n> Main Menu-------------(1)" + "\n> Continue Script-------(Any Other Key)\n>" + "---"*13 + "<\n\n> ")
        if "1" in toDo:
            cv2.destroyAllWindows()
            main()
        else:
            pass
    except Exception,e:
        if "something@R" in str(e):
            print "[Error] | Something Happaned."
        else:
            raw_input("[Error] | > " + str(e))
            cv2.destroyAllWindows()
            main()








def main():
    try:
        cls()
        chs = raw_input("""Example: "6 -hsv -glich"

> OpenCV Playground:           [Options]
>---------------------------------------------<
> ExtractColor-------------(1) []
> Corners------------------(2) []
> Detection----------------(3) []
> MotionTracking-----------(4) []
> OpticalFlow--------------(5) [-HSV, -GLICH]
> Facial Recognition-------(6) [Unfinished]
>---------------------------------------------<

> """)
        if "1" in chs:
            showBlue()
            main()
        elif "2" in chs:
            detectCorners()
            main()
        elif "3" in chs:
            objectDetection()
            main()
        elif "4" in chs:
            motionTracking()
            main()
        elif "5" in chs:
            hsv = False
            glich = False
            if "hsv" in chs.lower():
                hsv = True
            if "glich" in chs.lower():
                glich = True
            opticalFlow(glich, hsv)
            main()
        elif "6" in chs:
            facialRecognition()
            main()
        else:
            main()
    except KeyboardInterrupt:
        print "[Notice] | Exiting Application... | User Request."
        sys.exit()
    except Exception,e:
        if "something@R" in str(e):
            print "[Error] | Something Happaned."
        else:
            raw_input("[Error] | > " + str(e))
            main()
if __name__ == "__main__":
    main()


