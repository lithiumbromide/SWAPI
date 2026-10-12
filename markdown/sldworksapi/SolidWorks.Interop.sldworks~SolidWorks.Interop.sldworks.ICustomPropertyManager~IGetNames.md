---
title: "IGetNames Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "IGetNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetNames.html"
---

# IGetNames Method (ICustomPropertyManager)

Gets the names of the custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNames( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetNames(Count)
```

### C#

```csharp
System.string IGetNames(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetNames(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of custom properties

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the custom properties

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICustomPropertyManager::Count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Count.html) before calling this method.

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::GetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
