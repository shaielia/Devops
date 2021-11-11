properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
   stage("clone"){
       git "https://github.com/shaielia/Devops.git"
   } 
   stage("show files"){
       sh "ls -l"
       
   }
}
