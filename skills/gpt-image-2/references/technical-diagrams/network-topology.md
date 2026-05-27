# Network Topology Diagram Template

> ⚠️ **This template generates bitmap (PNG)**, not NetBox / Cisco Packet Tracer / draw.io editable network topologies.
> For editable diagrams use NetBox / Lucidchart / draw.io / Cisco Packet Tracer.

This file is used for generating "engineering-style network topology diagrams":

- Company / data center network topologies
- Multi-region / multi-zone deployment topologies
- Microservice / service mesh topologies
- VPC / subnet / routing table topologies
- Edge / CDN / multi-cloud interconnect topologies

Characteristics:

- Device nodes use typed glyphs: router (diamond with X cross) / switch (rectangle with multiple ports) / server (small chassis with cooling bars) / firewall (brick wall) / cloud (cloud shape) / DB (cylinder)
- Physical connections use thick lines, logical connections use dashed lines
- Large dashed boxes surround zones / VLANs / VPCs
- Bandwidth / protocol labels on lines (e.g. "10 Gbps" / "BGP" / "TLS 1.3")
- Dark grid + monospace font (following visual system)

## Scope

- Data center / server room network topologies
- Cloud architecture network topologies (VPC / subnet / NAT / IGW)
- Multi-region / multi-cloud interconnects
- Service mesh topologies
- Edge / CDN / public internet entry topologies

## When to use

- User mentions "network topology / deployment topology / VPC / subnet / data center / server room / service mesh"
- User wants standard "network device glyph + zone grouping + connection bandwidth annotation" network diagram
- User accepts bitmap output

Do NOT use for:

- User wants "application-layer system architecture" → use `technical-diagrams/system-architecture.md`
- User wants "business flow" → use `technical-diagrams/flowchart-decision.md`
- User wants "sequence diagram" → use `technical-diagrams/sequence-diagram.md`

## Missing Information Priority Question Order

1. Topology name ("AWS VPC topology / company server room topology / multi-region deployment")
2. Main zones / subnets / VPCs (recommend 2-5 zones)
3. Devices / instances within each zone (routers / switches / servers / DBs / load balancers)
4. Inter-zone connections (VPN / Peering / IGW / Direct Connect)
5. Connection protocols / bandwidth (optional)
6. Whether to label IP ranges / CIDRs
7. Aspect ratio (default 16:9 landscape)

## Main Template: Standard Cloud / Data Center Network Topology Diagram

📖 Description

The entire image is divided by zone / VPC into large dashed-box regions, with device nodes (with typed glyphs) placed within each region, connected by thick lines (labeled with bandwidth / protocol), with cross-zone connections using dedicated gateway / VPN nodes. Overall presented with engineering feel on a dark grid background.

📝 Prompt

```json
{
  "type": "Engineering-style network topology diagram",
  "goal": "Generate an engineering-style network topology diagram for deployment documentation / network architecture review / training materials",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "deep slate #0F172A with subtle 1px grid #1E293B at 32px spacing",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"AWS Multi-AZ VPC Topology\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"production · ap-northeast-1\"}",
    "position": "top-left, JetBrains Mono / SF Mono, light gray"
  },
  "device_glyphs": {
    "rule": "Each device type uses a unified minimalist geometric glyph, avoid using real vendor icons",
    "types": [
      { "type": "router", "glyph": "diamond shape with X cross inside", "color": "amber #FBBF24" },
      { "type": "switch", "glyph": "rectangle with multiple port dots along the bottom edge", "color": "amber #FBBF24" },
      { "type": "firewall", "glyph": "stylized brick wall pattern (small rectangles in 2-3 rows)", "color": "rose #FB7185" },
      { "type": "load_balancer", "glyph": "trapezoid funnel with 3 lines coming in, 1 going out", "color": "blue #60A5FA" },
      { "type": "server", "glyph": "small rack rectangle with 3-4 horizontal slots", "color": "emerald #34D399" },
      { "type": "container", "glyph": "rounded square with sail / shipping container symbol", "color": "emerald #34D399" },
      { "type": "database", "glyph": "cylinder (3D-suggested)", "color": "violet #A78BFA" },
      { "type": "cloud_service", "glyph": "cloud outline with abbreviation inside (e.g. 'S3', 'CDN')", "color": "cyan #22D3EE" },
      { "type": "user", "glyph": "stick figure", "color": "cyan #22D3EE" },
      { "type": "internet", "glyph": "globe with latitude / longitude lines", "color": "slate #94A3B8" },
      { "type": "nat_gateway", "glyph": "small rectangle labeled 'NAT'", "color": "amber #FBBF24" },
      { "type": "vpn_gateway", "glyph": "small rectangle with key icon, labeled 'VPN'", "color": "rose #FB7185" }
    ]
  },
  "zones": {
    "count": "{argument name=\"zone_count\" default=\"4\"}",
    "items": [
      { "id": "Z1", "label": "Public Internet", "color_border": "slate #94A3B8 dashed", "cidr": "0.0.0.0/0" },
      { "id": "Z2", "label": "VPC · ap-northeast-1\\n10.0.0.0/16", "color_border": "amber #FBBF24 dashed", "cidr": "10.0.0.0/16" },
      { "id": "Z3", "label": "Public Subnet · 10.0.1.0/24 (AZ-a)", "color_border": "blue #60A5FA dashed", "parent": "Z2" },
      { "id": "Z4", "label": "Private Subnet · 10.0.2.0/24 (AZ-a)", "color_border": "emerald #34D399 dashed", "parent": "Z2" }
    ],
    "zone_label_position": "top-left of each zone box, mono 11pt with CIDR on second line"
  },
  "nodes": {
    "items": [
      { "id": "N1", "type": "user", "label": "End Users", "zone": "Z1" },
      { "id": "N2", "type": "internet", "label": "Internet", "zone": "Z1" },
      { "id": "N3", "type": "cloud_service", "label": "CloudFront\\n(CDN)", "zone": "Z1" },
      { "id": "N4", "type": "load_balancer", "label": "ALB", "zone": "Z3" },
      { "id": "N5", "type": "nat_gateway", "label": "NAT GW", "zone": "Z3" },
      { "id": "N6", "type": "container", "label": "ECS Tasks\\n(2 instances)", "zone": "Z4" },
      { "id": "N7", "type": "database", "label": "RDS PostgreSQL\\n(Multi-AZ)", "zone": "Z4" },
      { "id": "N8", "type": "cloud_service", "label": "S3\\n(static assets)", "zone": "Z1" }
    ],
    "node_label_format": "device name + optional second line with detail (count / class / role), mono 10pt labeled below glyph"
  },
  "connections": {
    "items": [
      { "from": "N1", "to": "N2", "type": "physical", "label": "" },
      { "from": "N2", "to": "N3", "type": "physical", "label": "HTTPS / TLS 1.3" },
      { "from": "N3", "to": "N4", "type": "physical", "label": "Origin pull" },
      { "from": "N4", "to": "N6", "type": "physical", "label": "HTTP" },
      { "from": "N6", "to": "N7", "type": "physical", "label": "TCP 5432" },
      { "from": "N6", "to": "N5", "type": "physical", "label": "egress" },
      { "from": "N5", "to": "N2", "type": "physical", "label": "" },
      { "from": "N3", "to": "N8", "type": "physical", "label": "Origin pull" }
    ],
    "line_style": {
      "physical": "solid line 2px slate #94A3B8 (carries actual traffic)",
      "logical": "dashed line 1.5px slate #64748B (logical relation, e.g. 'IAM allows access')",
      "redundant": "double-line in violet #A78BFA (HA pair, redundant link)",
      "encrypted": "solid line 2px emerald #34D399 with small lock glyph in middle"
    },
    "label_format": "protocol + optional bandwidth, e.g. 'HTTPS / 443' / '10 Gbps' / 'BGP' / 'TLS 1.3', mono 9pt labeled at line center",
    "rule_routing": "Primarily orthogonal routing; cross-zone lines pass through zone boundaries"
  },
  "annotations": {
    "ip_cidr_labels": {
      "enabled": "{argument name=\"ip_labels_enabled\" default=\"true\"}",
      "rule": "Each zone labeled with CIDR; key nodes labeled with IP or hostname"
    },
    "az_labels": {
      "enabled": "{argument name=\"az_labels_enabled\" default=\"true\"}",
      "rule": "In cloud environments, label availability zones (AZ-a / AZ-b)"
    }
  },
  "legend": {
    "enabled": true,
    "position": "bottom-right",
    "content": "device glyph → device type, line style → connection type (physical / logical / redundant / encrypted), zone color → zone type",
    "style": "small panel, semi-transparent bg, mono 10pt"
  },
  "constraints": {
    "must_keep": [
      "Each device glyph consistent, no mixing",
      "Zones clearly enclosed with large dashed boxes",
      "Zone labels include CIDR / AZ (cloud) or VLAN ID (data center)",
      "Line thickness / color coding reflects connection type",
      "Dark grid background + monospace font",
      "Legend must be drawn"
    ],
    "avoid": [
      "Using real vendor logos (Cisco / AWS / Azure real icons) → risk of copyright infringement + breaks unified visual",
      "Inconsistent device glyphs (one uses a box, another uses a real icon)",
      "Using emoji as device icons",
      "Zones without dashed boxes → loses zone sense",
      "Connections without protocol labels → loses engineering value",
      "More than 15 nodes → crowded, consider splitting into sub-diagrams",
      "Using 3D / gradients / glass textures",
      "Claiming this is an editable SVG"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `title`, zones list (with CIDR / names), nodes list (with type + zone), connections (with from/to)
- **Can default**: `background` (dark grid), `device_glyphs` (default full set), `ip_labels_enabled` (true), `az_labels_enabled` (true)
- **Can randomize**: node placement positions (auto-layout within zones)

### Auto-Fill Strategy

- User provides "AWS single AZ VPC + ALB + ECS + RDS" → use default topology
- User doesn't provide CIDR → ask back (cannot fabricate IP ranges)
- User says "add multi-AZ HA" → duplicate private subnet to AZ-b, mark redundant connections
- User says "add WAF / Shield" → add firewall glyph before ALB
- User wants light mode → use Variant 1

## Variant 1: Light Network Topology

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC + faint grid #E2E8F0",
    "node_glyph_fill": "device color × 8% opacity",
    "node_glyph_border": "1.5px solid (deeper shade for white bg)",
    "label_color": "deep slate #0F172A",
    "zone_border_color": "deeper shade",
    "vibe": "white-background documentation / print edition"
  }
}
```

## Variant 2: Service Mesh Topology

```json
{
  "modify": {
    "title_format": "Service Mesh Topology",
    "node_emphasis": "Attach a small sidecar (proxy) glyph next to each service node, expressing the sidecar pattern",
    "connections_emphasis": "Service-to-service connections all pass through sidecars; mark mTLS encryption",
    "extras": "Can add a control plane node (Istio / Linkerd) in the upper right corner, with dashed lines representing control flow",
    "use_case": "Istio / Linkerd / Consul / Cilium service mesh documentation"
  }
}
```

Suitable for: service mesh architecture, zero-trust networking, SRE training materials.

## Variant 3: Multi-Cloud Interconnect Topology (Hybrid Cloud)

```json
{
  "modify": {
    "zones": "Arrange multiple cloud regions side by side in large boxes: 'AWS Region' + 'GCP Region' + 'On-Prem DC'",
    "interconnect": "Inter-cloud connections use 'Direct Connect' / 'Cloud Interconnect' / 'VPN' thick lines, labeled with bandwidth / SLA",
    "extras": "Can add transit gateway / central routing hub at canvas center",
    "use_case": "Hybrid cloud / multi-cloud architecture, disaster recovery topologies, migration planning"
  }
}
```

Suitable for: hybrid cloud architecture, multi-cloud deployment, disaster recovery / DR topologies.

## Things to Avoid

- Using real vendor icons (risk of copyright infringement)
- Inconsistent device glyphs (same device type using different shapes)
- Using emoji as device icons
- Zones without dashed boxes → loses zone sense
- Connections without protocol / bandwidth labels → loses engineering value
- More than 15 nodes → visual explosion
- Using 3D / gradients / glass textures (breaks engineering feel)
- Central hub-and-spoke without labeling what the center "does"
- Cramming "application layer" components into network topology (use system-architecture instead)
- Pretending this is an exportable editable SVG
- Missing IP / CIDR information (core information for cloud network diagrams)