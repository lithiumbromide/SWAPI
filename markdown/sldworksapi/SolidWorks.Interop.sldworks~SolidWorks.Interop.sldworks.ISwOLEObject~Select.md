---
title: "Select Method (ISwOLEObject)"
project: "SOLIDWORKS API Help"
interface: "ISwOLEObject"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Select.html"
---

# Select Method (ISwOLEObject)

Selects an OLE object.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal Append As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwOLEObject
Dim Append As System.Boolean
Dim value As System.Boolean

value = instance.Select(Append)
```

### C#

```csharp
System.bool Select(
   System.bool Append
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool Append
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the OLE object to the selection list, false replaces the selection list with this OLE object

### Return Value

True if the OLE object is selected, false if it is not

## VBA Syntax

See [SwOLEObject::Select](ms-its:sldworksapivb6.chm::/sldworks~SwOLEObject~Select.html).

## See Also

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.html)
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
