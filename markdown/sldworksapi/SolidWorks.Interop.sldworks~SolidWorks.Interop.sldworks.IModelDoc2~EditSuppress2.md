---
title: "EditSuppress2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditSuppress2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSuppress2.html"
---

# EditSuppress2 Method (IModelDoc2)

Suppresses the selected feature, the selected component, or the owning feature of the selected face.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditSuppress2() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.EditSuppress2()
```

### C#

```csharp
System.bool EditSuppress2()
```

### C++/CLI

```cpp
System.bool EditSuppress2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected feature, component, or owning feature of the selected face is suppressed, false if not

## VBA Syntax

See [ModelDoc2::EditSuppress2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditSuppress2.html).

## Examples

[Suppress Feature (VBA)](Suppress_Feature_Example_VB.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)

## Remarks

This routine is identical to the now obsolete IModelDoc2::EditSuppress. The version number was incremented to allow VB applications to take advantage of information not available in the now obsolete IPartDoc::EditSuppress2.

This method closes any component files when called in an assembly. If the components were modified, then those modifications are not automatically saved. You must save any modifications before the files are closed.

SOLIDWORKS does not allow suppressing features or components while a PropertyManager page is open.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditUnsuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppress2.html)
[IModelDoc2::EditUnsuppressDependent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppressDependent2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
