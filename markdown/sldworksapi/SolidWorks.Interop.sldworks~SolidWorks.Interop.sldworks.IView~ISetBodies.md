---
title: "ISetBodies Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ISetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetBodies.html"
---

# ISetBodies Method (IView)

Sets the bodies of a multibody part to include in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArray As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Count As System.Integer
Dim BodyArray As Body2

instance.ISetBodies(Count, BodyArray)
```

### C#

```csharp
void ISetBodies(
   System.int Count,
   ref Body2 BodyArray
)
```

### C++/CLI

```cpp
void ISetBodies(
   System.int Count,
   Body2^% BodyArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of bodies in a multibody part
- `BodyArray`: - in-process, unmanaged C++: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBodies.html)
[IView::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Bodies.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
