                              % classification test
% clear variable
clear;
clc;

% import data 
addpath('libsvm-3.25\matlab')
% import libsvm and data set
addpath('F:\github_lib\Opticalflow4HAR\libsvm-3.25\matlab');


train = load ('train_ratio.csv');
test = load ('test_ratio.csv');
% generate random number for divide data into training and test set.
%n = randperm(size(data,1));
%t = randperm(size(test,1));
%training set 
train_matrix = train(:,1:9); % training data 1-70,6 columns
train_label = train(:,10); % training label at 7 column.

% test train 
test_matrix = test(:,1:9);
test_label = test(:,10);

% data normalization
[train_matrix, PS] = mapminmax(train_matrix');
train_matrix = train_matrix';
test_matrix = mapminmax('apply',test_matrix', PS);
test_matrix = test_matrix';

model = svmtrain(train_label,train_matrix,'-s 0 -t 2 -c 1.2 -g 2.8 -b 1'); % -v-s 0 -t 2 -c 1.2 -g 2.8'

% simulation to test
[predict_label_1,accuracy_1,dec_value] = svmpredict(test_label,test_matrix,model,'-b 1'); % version ,match parameters

% drawing figure 
figure
plot(test_label,'b o');
hold on 
plot(predict_label_1,'r *');
 
grid on 
xlabel('samp_num');
ylabel('type');
legend('type_T');
set(gca,'fontsize',12)