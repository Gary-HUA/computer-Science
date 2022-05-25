clc;
clear ;
xe = [1,1,1,1,1,1,1,1,1,1,10,21,31,40,48,56,64,72,80,88,96,104,113,123,134,144,144,144,144,143,139,138,139,139,138,144,144,141,144,144,140,140,142,141,144,142,135,124,114,105,96,88,80,72,64,56,48,39,33,24,15,1,1,1,1,1,1,1,1,1,1,1];
ye = [83,77,70,64,56,49,40,30,19,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,17,29,39,49,58,65,71,78,84,89,96,102,109,116,121,129,138,147,162,173,180,180,180,180,180,180,180,180,180,180,180,180,172,172,171,174,160,149,139,130,123,115,109,102,96,89];
xc = 72;
yc = 89;
for inx =1:72
    disp(xe(inx));
    disp('=================');
    if (xe(inx)==xc)&&(yc==ye(inx))
        disp('the same point with centroid');
    continue;
    end
    if all(xc==xe(inx))||all(yc==ye(inx))
        disp('at 0|90 degree...');      
        continue;
    elseif (xe(inx)>xc)
        steps = 1;
    else
        steps = -1;
    end 

     k =((ye(inx)-yc)/(xe(inx)-xc));% k of  line equation
     fprintf('k= %f:',k);
     inin = 1;
    for  x = xc:steps:xe(inx)
        fprintf('x=%d',x);
        y =k*(x-(xc))+yc;
        y = round(y);
        fprintf('y=%d',y);
%         values = frameLogical(x,y);
        % fprintf('x=%d y=%d values=%d',x,y, values);
%         disp(values);
      
        
        
        
        
        
%         if values ~= swit
%       
%           % fprintf('count = %d',inin);
%          intersection_space = zeros(1,9);
%             intersection1st_distance = sqrt((xe(inx)-xCenter).^2+(ye(inx)-yCenter).^2);% first
%             intersection_space(1,1)= xe(inx);
%             intersection_space(1,2)= ye(inx);
%             intersection_space(1,3)=intersection1st_distance; 
%             intersection_space(1,4)=x;
%             intersection_space(1,5)=y;
%             intersectiontwo_distance = sqrt((x-xCenter).^2+(y-yCenter).^2);
%             intersection_space(1,6)=intersectiontwo_distance;
%             intersection_space(1,7) = intersection1st_distance/intersectiontwo_distance;
%             swit = values;
%             dlmwrite('intersection.csv',intersection_space,'-append'); 
%             continue;   
%         end 
    end
%     intersection_space1 = zeros(1,9);
%     intersection_distance = sqrt((xe(inx)-xCenter).^2+(ye(inx)-yCenter).^2);
%     intersection_space1(1,1)= xe(inx);
%     intersection_space1(1,2)= ye(inx);
%     intersection_space1(1,3)=intersection_distance;
%     
%     dlmwrite('intersection.csv',intersection_space1,'-append');
end 