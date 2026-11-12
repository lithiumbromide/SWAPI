---
title: "Select Method (IManipulator)"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Select.html"
---

# Select Method (IManipulator)

Select a manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select(Append, Data)
```

### C#

```csharp
System.bool Select(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the manipulator tot he selection list, false replaces the selection list with this manipulator
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the manipulator is selected, false if not

## VBA Syntax

See [Manipulator::Select](ms-its:sldworksapivb6.chm::/sldworks~Manipulator~Select.html).

## See Also

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
