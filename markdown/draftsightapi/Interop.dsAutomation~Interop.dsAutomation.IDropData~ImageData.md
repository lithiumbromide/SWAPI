---
title: "ImageData Property (IDropData)"
project: ""
interface: "IDropData"
member: "ImageData"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~ImageData.html"
---

# ImageData Property (IDropData)

Gets or sets the image stored in this drop's MIME data.

## Syntax

### Visual Basic

```vb
Property ImageData As System.Object
```

### C#

```csharp
System.object ImageData {get; set;}
```

### JScript

```
function get,set ImageData : System.Object
```

### Managed Extensions for C++

```
__property System.Object* get_ImageData();
__property void set_ImageData(
   System.Object* value
);
```

### C++/CLI

```cpp
property System.Object^ ImageData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Byte array

## Remarks

The setter of this property is valid only if [IDropData::HasImageData](Interop.dsAutomation~Interop.dsAutomation.IDropData~HasImageData.html) is true.

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)

## Availability

DraftSight 2020 SP3
