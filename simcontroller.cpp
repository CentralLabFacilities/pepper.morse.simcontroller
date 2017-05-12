#include "simcontroller.h"
#include "ui_simcontroller.h"

SimController::SimController(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SimController)
{
    ui->setupUi(this);
}

SimController::~SimController()
{
    delete ui;
}
