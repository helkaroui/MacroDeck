const { app, BrowserWindow, nativeTheme, screen } = require('electron/main')

try {
  require('electron-reloader')(module)
} catch (_) {}

const createWindow = () => {
  let display = screen.getPrimaryDisplay();
  let width = display.bounds.width;
  let height = display.bounds.height

  const win = new BrowserWindow({
    width: 700,
    height: 300,
    x: width - 700,
    y: height - 300,
    titleBarStyle: 'hidden',
    webPreferences: {
      nodeIntegration: true,
      //scrollBounce: true
    },
  })

  win.loadFile('src/pages/index.html')

  win.setResizable(false)
}

app.whenReady().then(() => {
  createWindow()


nativeTheme.themeSource = 'dark'

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
