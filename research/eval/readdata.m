function [content, label] = readdata()

    fileFolder = fullfile('./train_csv');
    dirOutput = dir(fullfile(fileFolder,'*.csv'));
    fileNames = {dirOutput.name}';

        % size(fileNames,1)
    label = [];
    for i = 1 : size(fileNames,1)
        S =  split(fileNames(i), '$');
        label = [label, str2num(S{2})];
    end
    % 
    content = [];
    for i = 1 : size(fileNames,1)
        path = "./train_csv/";
        name = fileNames(i);
        a = [];
        a = csvread(path + name);
    %     size(a,2)
        if size(a,2) > 91
            a = a(1:91);
        end
        while (91 - size(a,2)) ~= 0
    %         size(a)
            a = [a, 0];
    %         break
        end
        content = [content; a];
    %     break
    end
    % a = csvread("./test_csv/p24437_abiczo_1.py.csv")
end