#include<bits/stdc++.h>
using namespace std;

fstream ftrain;
fstream ftest;


class perceptron{
public:

    double fet1;
    double fet2;
    double fet3;
    int type;

};
//for train.txt
perceptron per[500];
perceptron bin[500];
perceptron error_track[500];

//for test.txt
perceptron test[500];
perceptron test_bin[500];

double w1=0;
double w2=0;
double w3=0;
double w4=0;

int make_binary() {
    int j=0;
//    for (int i=0;i<300;i++) {
//        if(per[i].type==1) {
//            bin[j]=per[i];
//            cout<<bin[j].type<<endl;
//            j++;
//        }
//    }
//    j--;
    //cout<<per[150].fet1<<" "<<per[160].fet2<<" "<<per[219].fet3<<" "<<per[299].type<<endl;
    return j;
}

int max_index(double a,double b,double c) {
    if(a>=b) {
        if(a>=c) return 1;
        else return 3;
    }
    else {
        if(b>=c) return 2;
        else return 3;
    }
}

int main() {
    ftrain.open("Train.txt");
    string s;
    perceptron per[300];
    int samples=0;
    while(getline(ftrain,s)) {
        ftrain>>per[samples].fet1>>per[samples].fet2>>per[samples].fet3>>per[samples].type;
        samples++;
    }

    samples--;
    //cout<<samples<<endl;
    //cout<<per[150].fet1<<" "<<per[160].fet2<<" "<<per[219].fet3<<" "<<per[299].type<<endl;
    //cout<<len<<endl;
    //int bin_len=make_binary();
    int j=0;
    for (int i=0;i<samples;i++) {
        if(per[i].type!=3) {
            bin[j]=per[i];
            //cout<<bin[j].type<<endl;
            j++;
        }
    }

    int bin_len=j;
    //cout<<bin_len;

    cout<<"*********Basic*********"<<endl<<endl;
    //string clss;
    int de=0;
    double w1_c=-100;
    while(w1!=w1_c) {
    //for(int k=0;k<100;k++) {
        de++;
        int ind=0;
        for(int i=0;i<bin_len;i++) {
            double fx=w1*bin[i].fet1+w2*bin[i].fet2+w3*bin[i].fet3+w4;
            if(fx>=0 && bin[i].type==2) {
                error_track[ind++]=bin[i];
            }
            else if(fx<0 && bin[i].type==1) {
                error_track[ind++]=bin[i];
            }

        }
        //cout<<ind<<endl;
        //cout<<error_track[80].fet1;
        w1_c=w1;
        for(int i=0;i<ind;i++) {
            if(error_track[i].type==1) {
                w1=w1+error_track[i].fet1;
                w2=w2+error_track[i].fet2;
                w3=w3+error_track[i].fet3;
            }
            else {
                w1=w1-error_track[i].fet1;
                w2=w2-error_track[i].fet2;
                w3=w3-error_track[i].fet3;
            }

        }

        for(int i=0;i<ind;i++) {
            error_track[i].fet1=0;
            error_track[i].fet2=0;
            error_track[i].fet3=0;
        }
        //cout<<"w1 "<<w1<<" w2 "<<w2<<" w3 "<<w3<<endl;

//        for(int i=0;<ind;i++) {
//            error_track[i]=none;
//        }
     }

     cout<<"w1 "<<w1<<" w2 "<<w2<<" w3 "<<w3<<endl;
     cout<<"# of iteration: "<<de<<endl;

     ftest.open("Test.txt");
     string s2;
     int samples2=0;
     while(!ftest.eof()) {
        ftest>>test[samples2].fet1>>test[samples2].fet2>>test[samples2].fet3>>test[samples2].type;
        samples2++;
     }
     samples2--;
     //cout<<samples2<<endl;
     //cout<<test[150].fet1<<" "<<test[160].fet2<<" "<<test[219].fet3<<" "<<test[299].type<<endl;


    int j1=0;
    int test_len=0;
    for (int i=0;i<samples2;i++) {
        if(test[i].type!=3) {
            test_bin[j1]=test[i];
            //cout<<bin[j].type<<endl;
            j1++;
        }
    }

    test_len=j1;
    //cout<<test_len<<endl;
    //cout<<test_bin[test_len-1].fet1;

    double basic_error=0;
    double basic_performance=0;
    for(int i=0;i<test_len;i++) {
        double fx2=w1*test_bin[i].fet1+w2*test_bin[i].fet2+w3*test_bin[i].fet3+w4;
        if(fx2>=0 && test_bin[i].type==2) basic_error++;
        else if(fx2<0 && test_bin[i].type==1) basic_error++;
    }

    cout<<"# of error: "<<basic_error<<endl;
    basic_performance=test_len-basic_error;
    basic_performance=(double)(basic_performance/test_len)*100;
    basic_error=(double)(basic_error/test_len)*100;
    cout<<"Performance: "<<basic_performance<<"%"<<endl;
    cout<<"Error: "<<basic_error<<"%"<<endl<<endl;
    cout<<"****************************"<<endl<<endl;

    cout<<"*********Reward & Punishment************"<<endl<<endl;

    w1=0;
    w2=0;
    w3=0;
    w4=1;

    double wrp=-100;
    int de2=0;
    while(w1!=wrp) {
    //for(int k=0;k<200;k++) {
        de2++;
        wrp=w1;
        for(int i=0;i<bin_len;i++) {
            double fx3=w1*bin[i].fet1+w2*bin[i].fet2+w3*bin[i].fet3+w4;
            if(fx3>=0 && bin[i].type==2) {
                //cout<<"i "<<i<<endl;
                w1=w1-bin[i].fet1;
                w2=w2-bin[i].fet2;
                w3=w3-bin[i].fet3;
            }
            else if(fx3<0 && bin[i].type==1) {
                //cout<<"i "<<i<<endl;
                w1=w1+bin[i].fet1;
                w2=w2+bin[i].fet2;
                w3=w3+bin[i].fet3;
            }

        }
    }

    cout<<"w1 "<<w1<<" w2 "<<w2<<" w3 "<<w3<<endl;
    cout<<"# of iteration: "<<de2<<endl;

    double reward_error=0;
    double reward_performance=0;
    for(int i=0;i<test_len;i++) {
        double fx4=w1*test_bin[i].fet1+w2*test_bin[i].fet2+w3*test_bin[i].fet3+w4;
        if(fx4>=0 && test_bin[i].type==2) reward_error++;
        else if(fx4<0 && test_bin[i].type==1) reward_error++;
    }

    cout<<"# of error "<<reward_error<<endl;
    reward_performance=test_len-reward_error;
    reward_performance=(double)(reward_performance/test_len)*100;
    reward_error=(double)(reward_error/test_len)*100;
    cout<<"Performance: "<<reward_performance<<"%"<<endl;
    cout<<"Error: "<<reward_error<<"%"<<endl<<endl;
    cout<<"****************************"<<endl<<endl;

    cout<<"************Pocket***************"<<endl<<endl;

    w1=0;
    w2=0;
    w3=0;
    w4=1;

    double d1=0;
    double d2=0;
    double d3=0;
    double accu=0;
    for(int k=0;k<100;k++) {
        //cout<<"asi"<<endl;
        for(int i=0;i<bin_len;i++) {
            double fx5=w1*bin[i].fet1+w2*bin[i].fet2+w3*bin[i].fet3+w4;
            if(fx5>=0 && bin[i].type==2) {
                    //cout<<"i "<<i<<endl;
                w1=w1-bin[i].fet1;
                w2=w2-bin[i].fet2;
                w3=w3-bin[i].fet3;
                break;
            }
            else if(fx5<0 && bin[i].type==1) {
                    //cout<<"i "<<i<<endl;
                w1=w1+bin[i].fet1;
                w2=w2+bin[i].fet2;
                w3=w3+bin[i].fet3;
                break;
            }

        }
        double temp_pocket_error=0;
        for(int i=0;i<bin_len;i++) {
            double fx6=w1*bin[i].fet1+w2*bin[i].fet2+w3*bin[i].fet3+w4;
            if(fx6>=0 && bin[i].type==2) temp_pocket_error++;
            else if(fx6<0 && bin[i].type==1) temp_pocket_error++;
        }
        double temp_acc=bin_len-temp_pocket_error;
        //cout<<"accuracy "<<accu<<endl;
        //cout<<"temp accuracy "<<temp_acc<<endl;
        if(temp_acc>accu) {
            //cout<<"yes"<<endl;
            accu=temp_acc;
            d1=w1;
            d2=w2;
            d3=w3;
            //cout<<"d1:"<<d1<<endl;
        }
        //else cout<<"no"<<endl;
    }

    w1=d1;
    w2=d2;
    w3=d3;

    cout<<"w1 "<<w1<<" w2 "<<w2<<" w3 "<<w3<<endl;
    //cout<<"# of iteration: "<<de2<<endl;

    double pocket_error=0;
    double pocket_performance=0;
    for(int i=0;i<test_len;i++) {
        double fx7=w1*test_bin[i].fet1+w2*test_bin[i].fet2+w3*test_bin[i].fet3+w4;
        if(fx7>=0 && test_bin[i].type==2) pocket_error++;
        else if(fx7<0 && test_bin[i].type==1) pocket_error++;
    }

    cout<<"# of error "<<pocket_error<<endl;
    pocket_performance=test_len-pocket_error;
    pocket_performance=(double)(pocket_performance/test_len)*100;
    pocket_error=(double)(pocket_error/test_len)*100;
    cout<<"Performance: "<<pocket_performance<<"%"<<endl;
    cout<<"Error: "<<pocket_error<<"%"<<endl<<endl;
    cout<<"****************************"<<endl<<endl;

    cout<<"************Kesler**************"<<endl<<endl;

    double kesler[2*samples][12];
    int klen=0;
    for(int i=0;i<samples;i++) {
        if(per[i].type==1) {
            kesler[klen][0]=per[i].fet1;
            kesler[klen][1]=per[i].fet2;
            kesler[klen][2]=per[i].fet3;
            kesler[klen][3]=1;
            kesler[klen][4]=-per[i].fet1;
            kesler[klen][5]=-per[i].fet2;
            kesler[klen][6]=-per[i].fet3;
            kesler[klen][7]=-1;
            kesler[klen][8]=0;
            kesler[klen][9]=0;
            kesler[klen][10]=0;
            kesler[klen][11]=0;

            kesler[klen+1][0]=per[i].fet1;
            kesler[klen+1][1]=per[i].fet2;
            kesler[klen+1][2]=per[i].fet3;
            kesler[klen+1][3]=1;
            kesler[klen+1][4]=0;
            kesler[klen+1][5]=0;
            kesler[klen+1][6]=0;
            kesler[klen+1][7]=0;
            kesler[klen+1][8]=-per[i].fet1;
            kesler[klen+1][9]=-per[i].fet2;
            kesler[klen+1][10]=-per[i].fet3;
            kesler[klen+1][11]=-1;
        }

        else if(per[i].type==2) {
            kesler[klen][0]=-per[i].fet1;
            kesler[klen][1]=-per[i].fet2;
            kesler[klen][2]=-per[i].fet3;
            kesler[klen][3]=-1;
            kesler[klen][4]=per[i].fet1;
            kesler[klen][5]=per[i].fet2;
            kesler[klen][6]=per[i].fet3;
            kesler[klen][7]=1;
            kesler[klen][8]=0;
            kesler[klen][9]=0;
            kesler[klen][10]=0;
            kesler[klen][11]=0;

            kesler[klen+1][0]=0;
            kesler[klen+1][1]=0;
            kesler[klen+1][2]=0;
            kesler[klen+1][3]=0;
            kesler[klen+1][4]=per[i].fet1;
            kesler[klen+1][5]=per[i].fet2;
            kesler[klen+1][6]=per[i].fet3;
            kesler[klen+1][7]=1;
            kesler[klen+1][8]=-per[i].fet1;
            kesler[klen+1][9]=-per[i].fet2;
            kesler[klen+1][10]=-per[i].fet3;
            kesler[klen+1][11]=-1;
        }

        else if(per[i].type==3) {
            kesler[klen][0]=-per[i].fet1;
            kesler[klen][1]=-per[i].fet2;
            kesler[klen][2]=-per[i].fet3;
            kesler[klen][3]=-1;
            kesler[klen][4]=0;
            kesler[klen][5]=0;
            kesler[klen][6]=0;
            kesler[klen][7]=0;
            kesler[klen][8]=per[i].fet1;
            kesler[klen][9]=per[i].fet2;
            kesler[klen][10]=per[i].fet3;
            kesler[klen][11]=1;

            kesler[klen+1][0]=0;
            kesler[klen+1][1]=0;
            kesler[klen+1][2]=0;
            kesler[klen+1][3]=0;
            kesler[klen+1][4]=-per[i].fet1;
            kesler[klen+1][5]=-per[i].fet2;
            kesler[klen+1][6]=-per[i].fet3;
            kesler[klen+1][7]=-1;
            kesler[klen+1][8]=per[i].fet1;
            kesler[klen+1][9]=per[i].fet2;
            kesler[klen+1][10]=per[i].fet3;
            kesler[klen+1][11]=1;
        }
        klen=klen+2;
    }

    //cout<<klen<<endl;
    double weight[12];
    for(int i=0;i<=11;i++) weight[i]=1;

    for(int k=0;k<100;k++) {
        for(int i=0;i<klen;i++) {
            double func=0;
            for(int m=0;m<12;m++) {
              func=func+weight[m]*kesler[i][m];
            }
            if(func<0) {
                //cout<<"k: "<<k<<endl;
                for(int m=0;m<12;m++) {
                    weight[m]=weight[m]+kesler[i][m];
               }
            }
        }

//        for(int m=0;m<12;m++) {
//                cout<<weight[m]<<endl;
//        }
    }

    for(int m=0;m<12;m++) {
        cout<<weight[m]<<endl;
    }

    double last[3*samples2][13];
    int final_len=0;
    for(int i=0;i<samples2;i++) {

        last[final_len][0]=test[i].type;
        last[final_len][1]=test[i].fet1;
        last[final_len][2]=test[i].fet2;
        last[final_len][3]=test[i].fet3;
        last[final_len][4]=1;
        last[final_len][5]=0;
        last[final_len][6]=0;
        last[final_len][7]=0;
        last[final_len][8]=0;
        last[final_len][9]=0;
        last[final_len][10]=0;
        last[final_len][11]=0;
        last[final_len][12]=0;

        last[final_len+1][0]=test[i].type;
        last[final_len+1][1]=0;
        last[final_len+1][2]=0;
        last[final_len+1][3]=0;
        last[final_len+1][4]=0;
        last[final_len+1][5]=test[i].fet1;
        last[final_len+1][6]=test[i].fet2;
        last[final_len+1][7]=test[i].fet3;
        last[final_len+1][8]=1;
        last[final_len+1][9]=0;
        last[final_len+1][10]=0;
        last[final_len+1][11]=0;
        last[final_len+1][12]=0;


        last[final_len+2][0]=test[i].type;
        last[final_len+2][1]=0;
        last[final_len+2][2]=0;
        last[final_len+2][3]=0;
        last[final_len+2][4]=0;
        last[final_len+2][5]=0;
        last[final_len+2][6]=0;
        last[final_len+2][7]=0;
        last[final_len+2][8]=0;
        last[final_len+2][9]=test[i].fet1;
        last[final_len+2][10]=test[i].fet2;
        last[final_len+2][11]=test[i].fet3;
        last[final_len+2][12]=1;

        final_len=final_len+3;
    }

    //cout<<final_len<<endl;

    int kes_error=0;
    for(int i=0;i<final_len;i=i+3) {
        double kf1=0;
        double kf2=0;
        double kf3=0;
        for(int m=0;m<12;m++) {
            kf1=kf1+weight[m]*last[i][m+1];
            kf2=kf2+weight[m]*last[i+1][m+1];
            kf3=kf3+weight[m]*last[i+2][m+1];
        }
        int ch=max_index(kf1,kf2,kf3);
        if(ch!=last[i][0]) kes_error++;

    }

    cout<<"# of error :"<<kes_error<<endl;
    double kes_performance=samples2-kes_error;
    kes_performance=(double)(kes_performance/samples2)*100;
    cout<<"Performance :"<<kes_performance<<"%"<<endl;
    cout<<"Error :"<<(100-kes_performance)<<"%"<<endl;
    cout<<"****************************"<<endl;

}
