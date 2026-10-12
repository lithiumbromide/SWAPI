---
title: "IGetDisplayData Method (ICThread)"
project: "SOLIDWORKS API Help"
interface: "ICThread"
member: "IGetDisplayData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetDisplayData.html"
---

# IGetDisplayData Method (ICThread)

Gets the display data for this cosmetic thread.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDisplayData() As DisplayData
```

### Visual Basic (Usage)

```vb
Dim instance As ICThread
Dim value As DisplayData

value = instance.IGetDisplayData()
```

### C#

```csharp
DisplayData IGetDisplayData()
```

### C++/CLI

```cpp
DisplayData^ IGetDisplayData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object

## VBA Syntax

See [CThread::IGetDisplayData](ms-its:sldworksapivb6.chm::/sldworks~CThread~IGetDisplayData.html).

## See Also

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html)
[ICThread::GetDisplayData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetDisplayData.html)
