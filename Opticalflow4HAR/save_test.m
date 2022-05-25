clc;
clear;
xc=88;
yc=161;%(x,y)
xe=[54,55,64,71,73,75,76,77,78,79,80,81,84,85,85,86,87,88,88,89,90,91,91,92,93,95,98,100,105,112,115,115,114,111,109,109,109,109,112,111,111,111,109,104,100,97,94,93,92,91,90,89,88,88,87,86,85,84,83,83,81,80,79,77,75,72,71,68,66,60,55,55];
ye=[158,155,155,155,154,154,153,153,152,151,151,150,153,153,153,153,153,153,153,153,153,153,153,153,153,152,151,151,149,147,149,151,154,157,159,161,163,165,168,170,172,175,176,175,174,172,171,171,171,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,169,168,167,166,164,161];
xCenter = 88.5883;
yCenter = 161.2104;
result = [];
disp(result);
for inx = 1:1:72
    disp(inx);
    disp('==============');
    if all(xe(inx)==xc)&& all(yc==ye(inx))
        disp('the same point with centroid');
    continue;
    end
    if all(xc==(xe(inx))) || all(yc==(ye(inx)))
        disp('at 0|90 degree...'); 
        intersection_space = zeros(1, 9);
        intersection_space(1,1)= xe(inx);
        intersection_space(1,2)= ye(inx);
        intersection_space(1,3)= sqrt((xe(inx)-xCenter).^2+(ye(inx)-yCenter).^2);
        
        continue;
    end
    if (xe(inx)>xc)
        steps = 1;
    else
        steps = -1;
    end 
     k =((ye(inx)-yc)/(xe(inx)-xc));% k of  line equation   
     count = 0;
    for  x = xc:steps:xe(inx)
        y =k*(x-(xc))+yc;
        y = round(y);
        fprintf('x=%d;   y =%d;  xe = %d; ye = %d;', x, y, xe(inx), ye(inx));
%         values = frameLogical(x,y);
        % fprintf('x=%d y=%d values=%d',x,y, values);
        % disp(values);
%         swit = frameLogical(xc,yc);
%            if values ~=swit 
%              count = 1:3:7;
%             intersection_space= zeros(1:9);
%             intersection_space(1,count)= x;
%             intersection_space(1,count+1)= y;
%             intersection_space(1,count+2)= sqrt((x-xCenter).^2+(y-yCenter).^2);
%             result = [result,intersection_space];
%             swit = values;
%            elseif count >7
%                break;
%            end 
    end 
%     if all(count == 0) && all(x == xe(inx))
%         intersection_space = zeros(1:9);
%         intersection_space(1,1)= xe(inx);
%         intersection_space(1,2)= ye(inx);
%         intersection_space(1,3)= sqrt((xe(inx)-xCenter).^2+(ye(inx)-yCenter).^2);
%         result = [result,intersection_space]; 
%     end 
%   inx = inx+1;
end 