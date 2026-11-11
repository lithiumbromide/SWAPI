---
title: "CreateLineStyle Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateLineStyle.html"
---

# CreateLineStyle Method (IApplication)

Creates a simple [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html).

## Syntax

### Visual Basic

```vb
Function CreateLineStyle( _
   ByVal Name As System.String, _
   ByVal FileName As System.String, _
   ByVal Description As System.String, _
   ByVal Pattern As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool CreateLineStyle(
   System.string Name,
   System.string FileName,
   System.string Description,
   System.string Pattern
)
```

### JScript

```
function CreateLineStyle(
   Name : System.String,
   FileName : System.String,
   Description : System.String,
   Pattern : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CreateLineStyle(
   System.string* Name,
   System.string* FileName,
   System.string* Description,
   System.string* Pattern
)
```

### C++/CLI

```cpp
System.bool CreateLineStyle(
   System.String^ Name,
   System.String^ FileName,
   System.String^ Description,
   System.String^ Pattern
)
```

### Parameters

- `Name`: Name for the simple LineStyle to create
- `FileName`: Path and file name to which to add the simple LineStyle (see **Remarks**)
- `Description`: Simple LineStyle description
- `Pattern`: Pattern that defines the simple LineStyle (see **Remarks**)

### Return Value

True if the simple LineStyle is created, false if not

## Remarks

Simple LineStyle definition files are stored in ASCII text files with **.lin** filename extensions.

| These values... | Specify and create these simple LineStyle patterns... |
| --- | --- |
| Positive decimals | Length of dashes |
| Negative decimals | Length of spaces |
| 0 (zero) | Dots |

You must call [ILineStyleManager::LoadLineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~LoadLineStyle.html) to load the simple LineStyle in a document before you can get the simple LineStyle.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::CreateLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateLineStyle.html)

## Availability

DraftSight V1R4.0
