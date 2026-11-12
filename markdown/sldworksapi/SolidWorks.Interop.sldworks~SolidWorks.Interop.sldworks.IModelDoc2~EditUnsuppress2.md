---
title: "EditUnsuppress2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditUnsuppress2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppress2.html"
---

# EditUnsuppress2 Method (IModelDoc2)

Unsuppresses the selected feature or component.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditUnsuppress2() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.EditUnsuppress2()
```

### C#

```csharp
System.bool EditUnsuppress2()
```

### C++/CLI

```cpp
System.bool EditUnsuppress2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected feature or component is unsuppressed, false if not

## VBA Syntax

See [ModelDoc2::EditUnsuppress2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditUnsuppress2.html).

## Examples

[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)

## Remarks

This routine is identical to the obsoleted IModelDoc2::EditUnsuppress. The version number was incremented to allow VB applications to take advantage of information not available in the obsoleted IPartDoc::EditUnsuppress.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditSuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSuppress2.html)
[IModelDoc2::EditUnsuppressDependent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppressDependent2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
