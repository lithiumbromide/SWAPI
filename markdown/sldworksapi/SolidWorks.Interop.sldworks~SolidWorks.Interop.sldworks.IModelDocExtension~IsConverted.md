---
title: "IsConverted Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IsConverted"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsConverted.html"
---

# IsConverted Method (IModelDocExtension)

Gets whether the active document was converted to the current release uponing opening but has not yet been saved.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsConverted() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.IsConverted()
```

### C#

```csharp
System.bool IsConverted()
```

### C++/CLI

```cpp
System.bool IsConverted();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the active document was converted to the current release uponing opening but not yet been saved, false if not

## VBA Syntax

See [ModelDocExtension::IsConverted](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IsConverted.html).

## Examples

**Visual Basic for Applications (VBA)**

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim bool As Boolean

Sub Main()

Set swApp = CreateObject("Sldworks.Application")
Set swModel = swApp.**ActiveDoc**
Set swModelDocExt = swModel.**Extension**
Debug.Print "Document converted to current release but not yet saved? " _

& swModelDocExt.**IsConverted**

End Sub

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
