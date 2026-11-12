---
title: "InsertExternalReferenceWithReferenceType Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertExternalReferenceWithReferenceType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertExternalReferenceWithReferenceType.html"
---

# InsertExternalReferenceWithReferenceType Method (ISketchManager)

Inserts an external reference to a Block instance with the specified reference type.

## Syntax

### Visual Basic

```vb
Function InsertExternalReferenceWithReferenceType( _
   ByVal PathName As System.String, _
   ByVal InsertX As System.Double, _
   ByVal InsertY As System.Double, _
   ByVal InsertZ As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Rotation As System.Double, _
   ByVal RefType As dsExternalReferenceType_e _
) As BlockInstance
```

### C#

```csharp
BlockInstance InsertExternalReferenceWithReferenceType(
   System.string PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation,
   dsExternalReferenceType_e RefType
)
```

### JScript

```
function InsertExternalReferenceWithReferenceType(
   PathName : System.String,
   InsertX : System.double,
   InsertY : System.double,
   InsertZ : System.double,
   Scale : System.double,
   Rotation : System.double,
   RefType : dsExternalReferenceType_e
) : BlockInstance;
```

### Managed Extensions for C++

```
BlockInstance* InsertExternalReferenceWithReferenceType(
   System.string* PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation,
   dsExternalReferenceType_e RefType
)
```

### C++/CLI

```cpp
BlockInstance^ InsertExternalReferenceWithReferenceType(
   System.String^ PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation,
   dsExternalReferenceType_e RefType
)
```

### Parameters

- `PathName`: Path and file name of the external reference to insert
- `InsertX`: x coordinate where to insert the external reference
- `InsertY`: y coordinate where to insert the external reference
- `InsertZ`: z coordinate where to insert the external reference
- `Scale`: Scale factor for each axis
- `Rotation`: Angle by which to rotate the external reference; in radians (see **Remarks**)
- `RefType`: Reference type as defined by [dsExternalReferenceType_e](Interop.dsAutomation~Interop.dsAutomation.dsExternalReferenceType_e.html)

### Return Value

[Block instance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)

## Remarks

Use a positive value for Rotation to rotate the external reference counterclockwise and a negative value to rotate the external reference clockwise.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::DetachExternalReference Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachExternalReference.html)

## Availability

DraftSight 2024 SP4
