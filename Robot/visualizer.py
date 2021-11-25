import os;
import matplotlib.pyplot as plt;

FolderPath = os.path.dirname(os.path.normpath(__file__));
InputFilePath = os.path.join(FolderPath, "robot.ki");

plt.grid(True);
plt.axis([0, 10, 0, 10]);

file = open(os.path.join(FolderPath, "robot.be"));
PackageCount = int(file.readline());
points = [];
for i in range(0, PackageCount):
    line = file.readline().split();
    points.append((int(line[0]), int(line[1])));
x = list(map(lambda x: x[0], points));
y = list(map(lambda x: x[1], points));
plt.scatter(x, y);

file.close();

file = open(InputFilePath);
points = [];
lines = file.readlines();
points = [];
for line in lines:
    line = line.split();
    points.append((int(line[0]), int(line[1])));

    x = list(map(lambda x: x[0], points));
    y = list(map(lambda x: x[1], points));

    plt.plot(x, y);
    plt.pause(0.5);

plt.show();