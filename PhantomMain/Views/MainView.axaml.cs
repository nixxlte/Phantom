using Avalonia.Controls;
using Avalonia.Interactivity;
using System.Diagnostics;

namespace PhantomMain.Views;

public partial class MainView : UserControl
{
    public MainView()
    {
        InitializeComponent();
    }
    private void RefreshButton_Click(object? sender, RoutedEventArgs e)
    {
        Debug.WriteLine("Refresh beta page");
    }
}
