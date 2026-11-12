---
title: "GetLinkPath Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "GetLinkPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetLinkPath.html"
---

# GetLinkPath Method (IEmbeddedObject)

Gets the full path and name of the file that is linked to this embedded object.

## Syntax

### Visual Basic

```vb
Function GetLinkPath() As System.String
```

### C#

```csharp
System.string GetLinkPath()
```

### JScript

```
function GetLinkPath() : System.String;
```

### Managed Extensions for C++

```
System.string* GetLinkPath();
```

### C++/CLI

```cpp
System.String^ GetLinkPath();
```

### Return Value

Full path and name of the linked file (see **Remarks**)

## Examples

[Insert Embedded Object (JavaScript)](Insert_Embedded_Object_Example_JS.htm)
[Insert Embedded Object (VB.NET)](Insert_Embedded_Object_Example_VBNET.htm)
[Insert Embedded Object (C#)](Insert_Embedded_Object_Example_CSharp.htm)
[Insert Embedded Object (VBA)](Insert_Embedded_Object_Example_VBA.htm)

## Remarks

This method is valid only if [IEmbeddedObject::GetType](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetType.html) returns [dsEmbeddedObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsEmbeddedObjectType_e.html).dsEmbeddedObjectType_Link.

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)

## Availability

DraftSight V1R1.4
