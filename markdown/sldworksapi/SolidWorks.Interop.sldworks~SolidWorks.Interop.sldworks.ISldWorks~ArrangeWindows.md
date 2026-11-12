---
title: "ArrangeWindows Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ArrangeWindows"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ArrangeWindows.html"
---

# ArrangeWindows Method (ISldWorks)

Arranges the open windows in SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ArrangeWindows( _
   ByVal Style As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Style As System.Integer

instance.ArrangeWindows(Style)
```

### C#

```csharp
void ArrangeWindows(
   System.int Style
)
```

### C++/CLI

```cpp
void ArrangeWindows(
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Type of arrangement where:

  - 0 = Cascade
  - 1 = Tile horizontally
  - 2 = Tile vertically

## VBA Syntax

See [SldWorks::ArrangeWindows](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ArrangeWindows.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Create and Arrange Windows (VBA)](Create_and_Arrange_Windows_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CreateNewWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateNewWindow.html)
