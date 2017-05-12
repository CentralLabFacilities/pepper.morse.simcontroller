#ifndef SIMCONTROLLER_H
#define SIMCONTROLLER_H

#include <QMainWindow>

namespace Ui {
class SimController;
}

class SimController : public QMainWindow
{
    Q_OBJECT

public:
    explicit SimController(QWidget *parent = 0);
    ~SimController();

private:
    Ui::SimController *ui;
};

#endif // SIMCONTROLLER_H
