---
title: "IGetOLEObjects Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetOLEObjects"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.html"
---

# IGetOLEObjects Method (IModelDocExtension)

Get the OLE objects.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetOLEObjects( _
   ByVal Options As System.Integer, _
   ByVal OleObjectCount As System.Integer, _
   ByRef LpOleObjects As SwOLEObject _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim OleObjectCount As System.Integer
Dim LpOleObjects As SwOLEObject

instance.IGetOLEObjects(Options, OleObjectCount, LpOleObjects)
```

### C#

```csharp
void IGetOLEObjects(
   System.int Options,
   System.int OleObjectCount,
   out SwOLEObject LpOleObjects
)
```

### C++/CLI

```cpp
void IGetOLEObjects(
   System.int Options,
   System.int OleObjectCount,
   [Out] SwOLEObject^ LpOleObjects
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Options as defined in [swOleObjectOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOleObjectOptions_e.html)
- `OleObjectCount`: Number of OLE objects
- `LpOleObjects`: - in-process, unmanaged C++: Pointer to an array of the [OLE objects](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IModelDocExtension::GetOLEObjectCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.html) to determine the size of the output array.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
