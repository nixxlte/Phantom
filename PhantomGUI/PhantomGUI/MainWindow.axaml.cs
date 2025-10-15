using Avalonia.Controls;

namespace PhantomGUI {
    public class MainWindowViewModel {
        public string pcNAME { get; set; } = "PhantomEmu";
        public string build { get; set; } = "50main";
    }
    public partial class MainWindow : Window {
        public MainWindow() {
            InitializeComponent();
            DataContext = new MainWindowViewModel();
        }
    }
}