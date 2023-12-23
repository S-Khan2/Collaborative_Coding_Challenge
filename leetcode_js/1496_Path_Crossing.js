
// Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
// You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
// Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
// thank you
// Link: https://leetcode.com/problems/path-crossing/?envType=daily-question&envId=2023-12-23

/**
 * @param {string} path
 * @return {boolean}
 */
var isPathCrossing = function(path) {
    var cords = {
        'N' : [0,1],
        'W': [-1,0],
        'E' : [1,0],
        'S': [0,-1]
    };
    var points_list = [[0,0]];
    for(let dir of path){
        var new_pos = new Array(2);
        new_pos[0] = cords[dir][0] + points_list[points_list.length -1][0];
        new_pos[1] = cords[dir][1] + points_list[points_list.length -1][1];
        for (let point of points_list){
            if (point[0] == new_pos[0] && point[1] == new_pos[1]){
                return true;
            }
        };
        points_list.push(new_pos);    
    };
    return false;
};

const path = "NESWW";
 
console.log(isPathCrossing(path));