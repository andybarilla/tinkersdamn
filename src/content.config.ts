import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders'; // Not available with legacy API

const blog = defineCollection({
    loader: glob({ pattern: "**/*.{md,mdx}", base: "./data/posts" }),
    schema: z.object({
        title: z.string(),
        pubDate: z.coerce.date(),
        description: z.string(),
        author: z.string(),
        tags: z.array(z.string()),
    })
});

export const collections = { blog };