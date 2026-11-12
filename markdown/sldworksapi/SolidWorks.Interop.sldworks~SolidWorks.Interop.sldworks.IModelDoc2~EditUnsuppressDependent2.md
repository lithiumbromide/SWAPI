---
title: "EditUnsuppressDependent2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditUnsuppressDependent2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppressDependent2.html"
---

# EditUnsuppressDependent2 Method (IModelDoc2)

Unsuppresses the selected feature or component and their dependents.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditUnsuppressDependent2() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.EditUnsuppressDependent2()
```

### C#

```csharp
System.bool EditUnsuppressDependent2()
```

### C++/CLI

```cpp
System.bool EditUnsuppressDependent2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected feature or component and their dependents are unsuppressed, false if not

## VBA Syntax

See [ModelDoc2::EditUnsuppressDependent2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditUnsuppressDependent2.html).

## Remarks

This method is identical to the obsoleted IModelDoc2::EditUnsuppressDependent method. The version number was incremented to allow Visual Basic applications to take advantage of information not available in the obsoleted IPartDoc::EditUnsuppressDependent method.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditSuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSuppress2.html)
[IModelDoc2::EditUnsuppress2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUnsuppress2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
